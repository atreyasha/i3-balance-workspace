# i3-balance-workspace

Balance windows and workspace sizes in i3wm. Functionality is similar to the `Emacs` command `M-x balance-windows`.

## Installation

Below are available options to install this python package:

1. Install from PyPi (Python Package Index) using `pip`:

```shell
$ pip install i3-balance-workspace
```

2. Install locally using `poetry`:

    a. Ensure `poetry` is installed on your system
    
    b. Clone this repository and navigate to its root folder
    
    c. Execute `poetry build`
    
    d. Execute `pip install dist/i3_balance_workspace-{meta-data}.whl`, where `{meta-data}` is some auto-generated variable.

Either of these options will install this package and place an executable `i3_balance_workspace` in a directory located in your `$PATH` variable. The exact location is dependant on the permissions you provided during installation.

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

In order to get the full benefit of this routine, it is recommended to create i3 keybindings for this command. Below is an example keybinding which can be appended to your i3 `config` file.

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
