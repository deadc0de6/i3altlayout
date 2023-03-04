[![Build Status](https://github.com/deadc0de6/i3altlayout/workflows/tests/badge.svg)](https://github.com/deadc0de6/i3altlayout/actions)
[![PyPI version](https://badge.fury.io/py/i3altlayout.svg)](https://badge.fury.io/py/i3altlayout)
[![Python](https://img.shields.io/pypi/pyversions/i3altlayout.svg)](https://pypi.python.org/pypi/i3altlayout)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

# I3ALTLAYOUT

`i3altlayout` helps you handle more efficiently your screen real estate in [i3wm](https://i3wm.org/)
by auto-splitting windows on their longest side.

If you open 4 windows, your workspace would look

```
             like this                               instead of this

+-----------------------------------+        +---------------------------------+
| +--------------+ +--------------+ |        | +-----+ +-----+ +-----+ +-----+ |
| |              | |              | |        | |     | |     | |     | |     | |
| |              | |      2       | |        | |     | |     | |     | |     | |
| |              | |              | |        | |     | |     | |     | |     | |
| |      1       | +--------------+ |        | |  1  | |  2  | |  3  | |  4  | |
| |              | +--------------+ |        | |     | |     | |     | |     | |
| |              | |      ||      | |        | |     | |     | |     | |     | |
| |              | |   3  ||  4   | |        | |     | |     | |     | |     | |
| +--------------+ +--------------+ |        | +-----+ +-----+ +-----+ +-----+ |
+-----------------------------------+        +---------------------------------+
```

---

# Installation

Install the script from [pypi](https://pypi.org/project/i3altlayout/)
```bash
$ sudo pip3 install i3altlayout
```

## Offline installation

Either install the dependencies and copy
the [i3altlayout.py file](/i3altlayout/i3altlayout.py):

* i3ipc (`python3-i3ipc` on debian/fedora)
* docopt (`python3-docopt` on debian/fedora)

Or package the pypi package:
```bash
## on online host
$ mkdir -p /tmp/i3altlayout && pip3 download -d /tmp/i3altlayout i3altlayout

## move the /tmp/i3altlayout directory to the offline host

## on offline host
$ sudo pip3 install --no-index --find-links=/tmp/i3altlayout i3altlayout
```

# Usage

Start the script directly with [i3](https://i3wm.org/) by adding it to your config file
(usually under `~/.config/i3/config`):
```
exec --no-startup-id "i3altlayout"
```

Or test it by running it from the command line (`i3altlayout`) and
open a few windows.

# Related projects

This project is similar to [i3-alternating-layout](https://github.com/olemartinorg/i3-alternating-layout)
but uses the [i3ipc library](https://github.com/acrisci/i3ipc-python)
instead of the unmaintained [i3-py library](https://github.com/ziberna/i3-py).

# Contribution

If you are having trouble installing or using `i3altlayout`, open an issue.

If you want to contribute, feel free to do a PR (please follow PEP8).

# License

This project is licensed under the terms of the GPLv3 license.
