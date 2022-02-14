#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import attrgetter
from typing import Iterable, Optional, cast
import argparse
import signal
import re


class Timeout:
    """
    Class to create a timeout setting in case resizing gets stuck on
    dead or problematic windows [source: https://stackoverflow.com/a/22348885]
    """
    def __init__(self, seconds, error_message='Process timed out'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class Sorting_Help_Formatter(argparse.HelpFormatter):
    """ Formatter for sorting argument options alphabetically """

    # source: https://stackoverflow.com/a/12269143
    def add_arguments(self, actions: Iterable[argparse.Action]) -> None:
        actions = sorted(actions, key=attrgetter("option_strings"))
        super(Sorting_Help_Formatter, self).add_arguments(actions)

    def _format_usage(self, usage: str, actions: Iterable[argparse.Action],
                      groups: Iterable[argparse._ArgumentGroup],
                      prefix: Optional[str]) -> str:
        if prefix is None:
            prefix = ("usage: ")

        # if usage is specified, use that
        if usage is not None:
            usage = usage % dict(prog=self._prog)

        # if no optionals or positionals are available, usage is just prog
        elif usage is None and not actions:
            usage = "%(prog)s" % dict(prog=self._prog)

        # if optionals and positionals are available, calculate usage
        elif usage is None:
            prog = "%(prog)s" % dict(prog=self._prog)

            # split optionals from positionals
            optionals = []
            positionals = []

            # split actions temporarily
            help_action = [
                action for action in actions if action.dest == "help"
            ]
            required_actions = sorted(
                [action for action in actions if action.required],
                key=attrgetter("option_strings"))
            optional_actions = sorted([
                action for action in actions
                if not action.required and action.dest != "help"
            ],
                                      key=attrgetter("option_strings"))

            # combine actions back
            actions = help_action + required_actions + optional_actions

            # proceed with usual
            for action in actions:
                if action.option_strings:
                    optionals.append(action)
                else:
                    positionals.append(action)

            # build full usage string
            format = self._format_actions_usage
            action_usage = format(optionals + positionals, groups)
            usage = " ".join([s for s in [prog, action_usage] if s])

            # wrap the usage parts if it's too long
            text_width = self._width - self._current_indent
            if len(prefix) + len(usage) > text_width:

                # break usage into wrappable parts
                part_regexp = (r"\(.*?\)+(?=\s|$)|"
                               r"\[.*?\]+(?=\s|$)|"
                               r"\S+")
                opt_usage = format(optionals, groups)
                pos_usage = format(positionals, groups)
                opt_parts = re.findall(part_regexp, opt_usage)
                pos_parts = re.findall(part_regexp, pos_usage)
                assert " ".join(opt_parts) == opt_usage
                assert " ".join(pos_parts) == pos_usage

                # helper for wrapping lines
                def get_lines(parts, indent, prefix=None):
                    lines = []
                    line = []
                    if prefix is not None:
                        line_len = len(prefix) - 1
                    else:
                        line_len = len(indent) - 1
                    for part in parts:
                        if line_len + 1 + len(part) > text_width and line:
                            lines.append(indent + " ".join(line))
                            line = []
                            line_len = len(indent) - 1
                        line.append(part)
                        line_len += len(part) + 1
                    if line:
                        lines.append(indent + " ".join(line))
                    if prefix is not None:
                        lines[0] = lines[0][len(indent):]
                    return lines

                # if prog is short, follow it with optionals or positionals
                if len(prefix) + len(prog) <= 0.75 * text_width:
                    indent = " " * (len(prefix) + len(prog) + 1)
                    if opt_parts:
                        lines = get_lines([prog] + opt_parts, indent, prefix)
                        lines.extend(get_lines(pos_parts, indent))
                    elif pos_parts:
                        lines = get_lines([prog] + pos_parts, indent, prefix)
                    else:
                        lines = [prog]

                # if prog is long, put it on its own line
                else:
                    indent = " " * len(prefix)
                    parts = opt_parts + pos_parts
                    lines = get_lines(parts, indent)
                    if len(lines) > 1:
                        lines = []
                        lines.extend(get_lines(opt_parts, indent))
                        lines.extend(get_lines(pos_parts, indent))
                    lines = [prog] + lines

                # join lines into usage
                usage = "\n".join(lines)

        # prefix with 'usage:'
        return "%s%s\n\n" % (prefix, usage)


class Metavar_Circum_Symbols(argparse.HelpFormatter):
    """
    Help message formatter which uses the argument 'type' as the default
    metavar value (instead of the argument 'dest')

    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    """
    def _get_default_metavar_for_optional(self,
                                          action: argparse.Action) -> str:
        """
        Function to return option metavariable type with circum-symbols
        """
        if action.type is not None:
            return "<" + action.type.__name__ + ">"  # type: ignore
        else:
            action.metavar = cast(str, action.metavar)
            return action.metavar

    def _get_default_metavar_for_positional(self,
                                            action: argparse.Action) -> str:
        """
        Function to return positional metavariable type with circum-symbols
        """
        if action.type is not None:
            return "<" + action.type.__name__ + ">"  # type: ignore
        else:
            action.metavar = cast(str, action.metavar)
            return action.metavar


class Metavar_Indenter(argparse.HelpFormatter):
    """
    Formatter for generating usage messages and argument help strings.

    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    """
    def _format_action(self, action: argparse.Action) -> str:
        """
        Function to define how actions are printed in help message
        """
        # determine the required width and the entry label
        help_position = min(self._action_max_length + 2,
                            self._max_help_position + 5)
        help_width = max(self._width - help_position, 11)
        action_width = help_position - self._current_indent - 2
        action_header = self._format_action_invocation(action)

        # no help; start on same line and add a final newline
        if not action.help:
            tup = self._current_indent, "", action_header
            action_header = "%*s%s\n" % tup

        # short action name; start on the same line and pad two spaces
        elif len(action_header) <= action_width:
            tup = self._current_indent, "", action_width, action_header  # type: ignore  # noqa: E501
            action_header = "%*s%-*s  " % tup  # type: ignore
            indent_first = 0

        # long action name; start on the next line
        else:
            tup = self._current_indent, "", action_header
            action_header = "%*s%s\n" % tup
            indent_first = help_position

        # collect the pieces of the action help
        parts = [action_header]

        # if there was help for the action, add lines of help text
        if action.help:
            help_text = self._expand_help(action)
            help_lines = self._split_lines(help_text, help_width)
            if action.nargs != 0 and action.type is not None:
                default = self._get_default_metavar_for_optional(action)
                args_string = self._format_args(action, default)
                parts.append("%*s%s\n" % (indent_first, "", args_string))
            elif action.type is None:
                args_string = "<flag>"
                parts.append("%*s%s\n" % (indent_first, "", args_string))
            else:
                parts.append("%*s%s\n" % (indent_first, "", help_lines[0]))
                help_lines.pop(0)
            for line in help_lines:
                parts.append("%*s%s\n" % (help_position, "", line))

        # or add a newline if the description doesn't end with one
        elif not action_header.endswith("\n"):
            parts.append("\n")

        # if there are any sub-actions, add their help as well
        for subaction in self._iter_indented_subactions(action):
            parts.append(self._format_action(subaction))

        # return a single string
        return self._join_parts(parts)

    def _format_action_invocation(self, action: argparse.Action) -> str:
        """
        Lower function to define how actions are printed in help message
        """
        if not action.option_strings:
            default = self._get_default_metavar_for_positional(action)
            metavar, = self._metavar_formatter(action, default)(1)
            return metavar
        else:
            parts = []  # type: ignore
            parts.extend(action.option_strings)
            return ", ".join(parts)


class ArgparseFormatter(argparse.ArgumentDefaultsHelpFormatter,
                        Metavar_Circum_Symbols, Metavar_Indenter,
                        Sorting_Help_Formatter):
    """
    Class to combine argument parsers in order to display meta-variables
    and defaults for arguments
    """
    pass
