## Table of Contents
-   [Tasks](#tasks)
    -   [Current release](#current-release)
    -   [Future releases](#future-releases)
        -   [add balance workspace test with fixtures and fake trees to
            simulate handling of simple/difficult
            cases](#add-balance-workspace-test-with-fixtures-and-fake-trees-to-simulate-handling-of-simpledifficult-cases)
        -   [look into more efficient workspace tree refreshing with
            connection to private i3ipc sync
            function](#look-into-more-efficient-workspace-tree-refreshing-with-connection-to-private-i3ipc-sync-function)
        -   [replace while loop with deterministic for loop in recursive
            adjustment where the effect of each size change is checked
            next to adjacent window and this is done until no negative
            size effects are found -\> essentially pre-empt the \"cannot
            resize\" error by checking these sizes beforehand to prevent
            loss of some windows -\> useful for edge cases where windows
            are made so small that they get corrupted, \"cannot resize\"
            seems to kick in after erroneous resizes in some cases which
            allows for negative
            dimensions](#replace-while-loop-with-deterministic-for-loop-in-recursive-adjustment-where-the-effect-of-each-size-change-is-checked-next-to-adjacent-window-and-this-is-done-until-no-negative-size-effects-are-found---essentially-pre-empt-the-cannot-resize-error-by-checking-these-sizes-beforehand-to-prevent-loss-of-some-windows---useful-for-edge-cases-where-windows-are-made-so-small-that-they-get-corrupted-cannot-resize-seems-to-kick-in-after-erroneous-resizes-in-some-cases-which-allows-for-negative-dimensions)
        -   [add new features such as balance vertical/horizontal and
            balance all
            workspaces](#add-new-features-such-as-balance-verticalhorizontal-and-balance-all-workspaces)
        -   [add specific debug script to find sources of errors when
            they do
            occur](#add-specific-debug-script-to-find-sources-of-errors-when-they-do-occur)
        -   [add specific changelog (with versions and updates) and
            todo\'s file, have them for different
            purposes](#add-specific-changelog-with-versions-and-updates-and-todos-file-have-them-for-different-purposes)

# Tasks

## Current release

## Future releases

### add balance workspace test with fixtures and fake trees to simulate handling of simple/difficult cases

1.  separate tests for gaps and non-gaps

2.  add test dependencies such as pytest and Xvfb

3.  try to capture various aspects by emulating python-i3ipc

4.  add local machine tests before installation

5.  add tests with different virtual environments for dependency
    versions

### look into more efficient workspace tree refreshing with connection to private i3ipc sync function

### replace while loop with deterministic for loop in recursive adjustment where the effect of each size change is checked next to adjacent window and this is done until no negative size effects are found -\> essentially pre-empt the \"cannot resize\" error by checking these sizes beforehand to prevent loss of some windows -\> useful for edge cases where windows are made so small that they get corrupted, \"cannot resize\" seems to kick in after erroneous resizes in some cases which allows for negative dimensions

### add new features such as balance vertical/horizontal and balance all workspaces

### add specific debug script to find sources of errors when they do occur

### add specific changelog (with versions and updates) and todo\'s file, have them for different purposes
