[![Build Status](https://travis-ci.org/deadc0de6/i3altlayout.svg?branch=master)](https://travis-ci.org/deadc0de6/i3altlayout)
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
sudo pip3 install i3altlayout
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
instead of the unmaintained [i3-py module](https://github.com/ziberna/i3-py).

# Contribution

If you are having trouble installing or using `i3altlayout`, open an issue.

If you want to contribute, feel free to do a PR (please follow PEP8).

# License

This project is licensed under the terms of the GPLv3 license.
