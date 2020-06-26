# i3-balance-workspace

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/atreyasha/i3-balance-workspace?color=green&label=release&logo=GitHub)
![PyPI](https://img.shields.io/pypi/v/i3-balance-workspace?color=green)
![AUR version](https://img.shields.io/aur/version/i3-balance-workspace-git?color=green&logo=Arch%20Linux)

Balance windows and workspaces in i3wm. Functionality is similar to the `Emacs` command `M-x balance-windows`.

## Installation

1. Install from PyPi (Python Package Index) using `pip`:

```shell
$ pip install i3-balance-workspace
```

2. For Arch-Linux users, install `i3-balance-workspace-git` via the [AUR](https://aur.archlinux.org/packages/i3-balance-workspace-git/).

## Usage

```
usage: i3_balance_workspace [-h] [--scope {workspace,focus}] [--timeout <int>]

optional arguments:
  -h, --help  show this help message and exit
  --scope     {workspace,focus}
              scope of resizing containers (default: workspace)
  --timeout   <int>
              timeout in seconds for resizing (default: 1)
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

```config
bindsym $mod+b exec "i3_balance_workspace --scope focus"
bindsym $mod+Shift+b exec "i3_balance_workspace"
```

## Examples

`i3-balance-workspace` has been tested and shows good performance on both simple and complex workspace layouts. Take a look at some examples:

### Scope: Workspace

<p align="center">
<img src="https://raw.githubusercontent.com/atreyasha/i3-balance-workspace/master/img/workspace.gif" width="800">
</p>

### Scope: Focused windows

<p align="center">
<img src="https://raw.githubusercontent.com/atreyasha/i3-balance-workspace/master/img/windows.gif" width="800">
</p>

## Bugs

In case of any bugs, feel free to open a GitHub issue.

## Developments

Further developments to this repository are summarized in our [change-log](https://github.com/atreyasha/i3-balance-workspace/blob/master/docs/todos.md).
