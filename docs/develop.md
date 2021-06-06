## Table of Contents
-   [Tasks](#tasks)

### Tasks

1.  Current

    1.  add balance workspace test with fixtures and fake trees to
        simulate handling of simple/difficult cases, separate tests for
        gaps and non-gaps, add test dependencies such as pytest and
        Xvfb, try to capture various aspects by emulating python-i3ipc

    2.  loosen pypi `i3ipc` version bound to allow more generous
        installations

    3.  consider applying same `python-i3ipc` bounds on the PKGBUILD,
        `>=2.2.1-2` -\> maybe not necessary since this won\'t affect
        much

    4.  change imports from in `__init__.py`, since only main is needed

    5.  clean code structure for repository once tests are added

    6.  look into more efficient workspace tree refreshing with
        connection to private i3ipc sync function

2.  Long-term

    1.  replace while loop with deterministic for loop in recursive
        adjustment where the effect of each size change is checked next
        to adjacent window and this is done until no negative size
        effects are found -\> essentially pre-empt the \"cannot resize\"
        error by checking these sizes beforehand to prevent loss of some
        windows -\> useful for edge cases where windows are made so
        small that they get corrupted, \"cannot resize\" seems to kick
        in after erroneous resizes in some cases which allows for
        negative dimensions

    2.  add new features such as balance vertical/horizontal and balance
        all workspaces

    3.  add specific debug script to find sources of errors when they do
        occur

    4.  add specific changelog (with versions and updates) and todo\'s
        file, have them for different purposes
