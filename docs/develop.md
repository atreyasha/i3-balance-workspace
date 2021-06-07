## Table of Contents
-   [Tasks](#tasks)
    -   [Current release](#current-release)
    -   [Future releases](#future-releases)

## Tasks

### Current release

1.  improve `refresh_workspace` workflow by using `i3` as a global
    variable and query directly

    1.  this should save some computation and reduce the need to
        re-compute this constantly

2.  improve versioning commands with regex substitutions -\> make them
    more robust

3.  re-do screencasts with keyboard capturing for posterity

4.  re-order repo skeleton to make things tighter -\> eg. add `img` into
    `docs`

    1.  improve `utils` code with more updated standards

5.  look into `__init__.py` file and what contents should be inside it

6.  look deeper into how imports are handled with dot importing

7.  add pipeline for `mypy` as a simpler code-checker

8.  replace `pkgrel` in `PKGBUILD` with `1` instead of `3`

    1.  add `aur-release` argument parsing as per `Makefile` in
        `downgrade`

9.  look into simplifying executable name where dashes are used instead
    -\> simply rename file in `pyproject.toml`

    1.  consider adding deprecation message or other fallbacks for
        backward compatibility -\> for example releasing two executables

    2.  release with major version bump for this change

    3.  update own configurations after that

### Future releases

1.  add balance workspace test with fixtures and fake trees to simulate
    handling of simple/difficult cases

    1.  separate tests for gaps and non-gaps

    2.  add test dependencies such as pytest and Xvfb

    3.  try to capture various aspects by emulating python-i3ipc

    4.  add local machine tests before installation

    5.  add tests with different virtual environments for dependency
        versions

2.  replace while loop with deterministic for loop in recursive
    adjustment where the effect of each size change is checked next to
    adjacent window and this is done until no negative size effects are
    found -\> essentially pre-empt the \"cannot resize\" error by
    checking these sizes beforehand to prevent loss of some windows -\>
    useful for edge cases where windows are made so small that they get
    corrupted, \"cannot resize\" seems to kick in after erroneous
    resizes in some cases which allows for negative dimensions

3.  add new features such as balance vertical/horizontal and balance all
    workspaces

4.  add specific debug script to find sources of errors when they do
    occur

5.  add specific changelog (with versions and updates) and todo\'s file,
    have them for different purposes
