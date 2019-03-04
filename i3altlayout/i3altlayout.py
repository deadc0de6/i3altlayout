#!/usr/bin/env python3
# author: deadc0de6

"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2019, deadc0de6
i3wm efficient screen real estate
"""

import sys
import os
import i3ipc
from docopt import docopt


NAME = 'i3altlayout'
VERSION = '0.2'
DEBUG = False
USAGE = """
{0}

Usage:
    {1} [-d] [--pid=<path>] [--socket=<path>]
    {1} --help
    {1} --version

Options:
    -d --debug          Enable debug logs.
    -p --pid=<path>     Write pid to file.
    -s --socket=<path>  i3 socket path.
    -v --version        Show version.
    -h --help           Show this screen.
""".format(NAME, NAME)


def log(string):
    """write logs to stderr"""
    if not DEBUG:
        return
    sys.stderr.write('{}\n'.format(string))


def on_window_focus(i3, event):
    """split depending on window size"""
    window = i3.get_tree().find_focused()
    log('new focused window: {}'.format(window))
    if not window:
        return
    if not window.rect:
        return
    if window.layout in ['stacked', 'tabbed']:
        return
    log('is a valid window')

    height = window.rect.height
    width = window.rect.width
    log('height: {}, width: {}'.format(height, width))

    if height > width:
        layout = 'vertical'
    else:
        layout = 'horizontal'
    cmd = 'split {}'.format(layout)
    log('running command: {}'.format(cmd))
    i3.command(cmd)
    log('\n')


def write_pid(path):
    """write our pid to file"""
    if not path:
        return
    pid = str(os.getpid())
    with open(path, 'w') as f:
        f.write(pid)


def main():
    """entry point"""
    args = docopt(USAGE, version=VERSION)
    global DEBUG
    DEBUG = args['--debug']
    spath = args['--socket']
    ppath = args['--pid']

    write_pid(ppath)

    try:
        i3 = i3ipc.Connection(socket_path=spath)
    except Exception as e:
        print(e)
        return False
    i3.on('window::focus', on_window_focus)
    try:
        i3.main()
    except KeyboardInterrupt:
        pass
    return True


if __name__ == "__main__":
    if main():
        sys.exit(0)
    sys.exit(1)
