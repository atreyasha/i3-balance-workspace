# i3-balance-workspace

[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/atreyasha/i3-balance-workspace?color=brightgreen&label=release&logo=GitHub)](https://github.com/atreyasha/i3-balance-workspace/tags)
[![PyPI](https://img.shields.io/pypi/v/i3-balance-workspace?color=brightgreen&logo=pypi&logoColor=yellow)](https://pypi.org/project/i3-balance-workspace/)
[![AUR version](https://img.shields.io/aur/version/i3-balance-workspace?color=brightgreen&logo=Arch%20Linux)](https://aur.archlinux.org/packages/i3-balance-workspace/)

Balance windows and workspaces in i3wm. Functionality is similar to the `Emacs` command `M-x balance-windows`.

## Installation

Following are available options to install `i3-balance-workspace`:

1. Install from PyPi (Python Package Index) using `pip`:

    ```shell
    $ pip install i3-balance-workspace
    ```

2. For Arch-Linux users, install `i3-balance-workspace` via the [AUR](https://aur.archlinux.org/packages/i3-balance-workspace/).

3. To install locally, ensure `poetry` and `pip` are installed on your system. Then execute:

    ```shell
    $ make install
    ```

## Usage

```
usage: i3_balance_workspace [-h] [--scope {workspace,focus}] [--timeout <int>]

options:
  --scope     {workspace,focus}
              scope of resizing containers (default: workspace)
  --timeout   <int>
              timeout in seconds for resizing (default: 1)
  -h, --help  <flag>
              show this help message and exit
```

In order to balance all windows in the current workspace, simply execute:

```shell
$ i3_balance_workspace
```

Alternatively, it is possible to only balance the windows that are in focus. For this, execute the following:

```shell
$ i3_balance_workspace --scope focus
```

In order to get the full benefit of this routine, it is recommended to initialize i3 persistent keybindings. Below are example keybindings which can be appended to your i3 `config` file.

```shell
bindsym $mod+b exec "i3_balance_workspace --scope focus"
bindsym $mod+Shift+b exec "i3_balance_workspace"
```

## Examples

`i3-balance-workspace` has been tested and shows good performance on both simple and complex workspace layouts. Take a look at some examples:

### Scope: Workspace

<p align="center">
<img src="https://raw.githubusercontent.com/atreyasha/i3-balance-workspace/main/docs/workspace.gif" width="800">
</p>

### Scope: Focused windows

<p align="center">
<img src="https://raw.githubusercontent.com/atreyasha/i3-balance-workspace/main/docs/windows.gif" width="800">
</p>

## Bugs

In case of any bugs, feel free to open a GitHub issue.

## Developments

Further developments to this repository are summarized in our development [log](https://github.com/atreyasha/i3-balance-workspace/blob/main/docs/develop.md).
