## Table of Contents
-   [Tasks](#tasks)
    -   [Future releases](#future-releases)

## Tasks

### Future releases

1.  add unit tests with fake trees

    1.  separate tests for gaps and non-gaps

    2.  add test dependencies such as pytest and Xvfb

    3.  try to capture various aspects by emulating python-i3ipc

    4.  add local machine tests before installation

    5.  add tests with different virtual environments for dependency
        versions

2.  improve modularity of code and rename functions to more idiomatic
    variants

    1.  improve `refresh_workspace` workflow by using `i3` as a global
        variable and query directly

    2.  re-think necessity of timeout function -\> or find easy
        cross-platform alternative

    3.  use more pythonic evaluations for variables and lengths in
        if-statements

3.  replace while loop with deterministic for loop in recursive
    adjustment

    1.  effect of each size change is checked next to adjacent window
        and this is done until no negative size effects are found

    2.  essentially pre-empt the \"cannot resize\" error by checking
        these sizes beforehand to prevent loss of some windows

    3.  useful for edge cases where windows are made so small that they
        get corrupted

    4.  \"cannot resize\" seems to kick in after erroneous resizes in
        some cases which allows for negative dimensions

4.  add new features such as balance vertical/horizontal and balance all
    workspaces

5.  add specific debug script to find sources of errors when they do
    occur

6.  add specific changelog (with versions and updates) and todo\'s file,
    have them for different purposes

7.  re-do screencasts with keyboard capturing for posterity

8.  look into simplifying executable name where dashes are used instead
    -\> simply rename file in `pyproject.toml`

    1.  consider adding deprecation message or other fallbacks for
        backward compatibility -\> for example releasing two executables
        -\> add debug message into i3 header for indication

    2.  release with major version bump for this change

    3.  update own configurations after that

    4.  update readme with new usage and warning as well

9.  add readme details for development install

    1.  add details of initializing pre-commit hook

    2.  add details on replicating virtual environment with lock files

    3.  add details on running various tests with `pytest` and `mypy`
