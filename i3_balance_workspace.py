#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import i3ipc
import argparse
import signal
from typing import List, Dict
from argparse import Namespace
from i3ipc import Con, CommandReply


class arg_metav_formatter(argparse.ArgumentDefaultsHelpFormatter,
                          argparse.MetavarTypeHelpFormatter):
    """
    Class to combine argument parsers in order to display meta-variables
    and defaults for arguments
    """
    pass


class timeout:
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


def refresh_workspace() -> Con:
    """
    Function refreshes i3 connection and returns the latest workspace container

    Returns:
        workspace (Con): workspace container
    """
    i3 = i3ipc.Connection()
    workspace = i3.get_tree().find_focused().workspace()
    return workspace


def adjust_container(container: Con, ideal_dim: float,
                     direction: str) -> CommandReply:
    """
    Function to deterministically adjust a single container

    Args:
        container (Con): Container to adjust
        ideal_dim (float): Target dimension in pixels
        direction (str): Direction in which growing/shrinking should happen

    Returns:
        reply (CommandReply): Reply of resizing command given to i3
    """
    current_dims = [container.rect.width, container.rect.height]
    if direction == "width":
        diff = ideal_dim - current_dims[0]
        if diff >= 0:
            reply = container.command("resize grow right %d px" % diff)
        else:
            reply = container.command("resize shrink right %d px" % abs(diff))
    elif direction == "height":
        diff = ideal_dim - current_dims[1]
        if diff >= 0:
            reply = container.command("resize grow down %d px" % diff)
        else:
            reply = container.command("resize shrink down %d px" % abs(diff))
    return reply


def recursive_adjustment(containers: List[Con], ids: List[int],
                         dim: str) -> None:
    """
    Function to recursively adjust list of containers at a given tree level

    Args:
        containers (List[Con]): List of containers to recursively adjust
        ids (List[int]): List of id's of respective containers
        dim (str): Which dimension to address during adjustment
    """
    redo = True
    counter = 0
    ideal_dim = (
        sum([getattr(container.rect, dim)
             for container in containers]) / len(containers))
    while redo and counter < (len(containers) - 1):
        redo = False
        for i in range(len(containers) - 1):
            reply = adjust_container(containers[i], ideal_dim, dim)
            if reply[0].error is not None:
                if reply[0].error == "Cannot resize.":
                    redo = True
            workspace = refresh_workspace()
            containers = [workspace.find_by_id(ID) for ID in ids]
        counter += 1


def balance_containers(containers: List[Con]) -> None:
    """
    Function to balance list of containers

    Args:
        containers (List[Con]): List of containers to recursively adjust
    """
    ids = [container.id for container in containers]
    adjust_heights = not all(container.rect.height == containers[0].rect.height
                             for container in containers)
    adjust_widths = not all(container.rect.width == containers[0].rect.width
                            for container in containers)
    if adjust_widths:
        recursive_adjustment(containers, ids, "width")
    if adjust_heights:
        recursive_adjustment(containers, ids, "height")


def traverse_workspace(workspace: Con) -> Dict[int, List[List[Con]]]:
    """
    Function to traverse and parse the workspace tree by level

    Args:
        workspace (Con): Workspace container

    Returns:
        level_nodes (Dict[int, List[List[Con]]]): Dictionary mapping of
        workspace tree
    """
    node_collection = workspace.nodes
    level_nodes = {0: [node_collection]}
    i = 1
    while True:
        node_collection = [
            node.nodes for node_list in level_nodes[i - 1]
            for node in node_list if len(node.nodes) > 0
        ]
        if len(node_collection) > 0:
            level_nodes[i] = node_collection
            if any(
                    len(node.nodes) > 0 for node_list in level_nodes[i]
                    for node in node_list):
                i += 1
            else:
                break
        else:
            break
    return level_nodes


def main(args: Namespace) -> None:
    """
    Main function to balance i3 window sizes with timeout as failsafe
    in case of problematic recursions or stale windows

    Args:
        args (Namespace): Argument namespace parsed via command-line
    """
    workspace = refresh_workspace()
    workspace_tree = traverse_workspace(workspace)
    with timeout(seconds=args.timeout):
        for i in reversed(workspace_tree.keys()):
            print(i)
            for j in range(len(workspace_tree[i])):
                containers = workspace_tree[i][j]
                containers = [
                    container for container in containers
                    if container.rect.width <= workspace.rect.width
                    and container.rect.height <= workspace.rect.height
                ]
                if len(containers) > 0:
                    balance_containers(containers)
                    workspace = refresh_workspace()
                    workspace_tree = traverse_workspace(workspace)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=arg_metav_formatter)
    parser.add_argument("--timeout",
                        type=int,
                        default=1,
                        help="timeout in seconds for resizing")
    args = parser.parse_args()
    main(args)
