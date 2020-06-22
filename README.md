# i3-balance-workspace
i3 IPC routine for balancing window sizes in the currently active workspace. Functionality is similar to the `Emacs` command `M-x balance-windows`.

## Dependencies

1. Python versions 3.5+, as the python script here uses typing features
2. `i3ipc` implemented in/for `python`, which can be installed with the explicit version (used for development) by running `pip install -r requirements.txt`

## Usage

```
usage: i3_balance_workspace.py [-h] [--timeout int]

optional arguments:
  -h, --help     show this help message and exit
  --timeout int  timeout in seconds for resizing (default: 2
```

In order to balance all windows/containers in the current workspace, simply execute:

```shell
./i3_balance_workspace.py
```
