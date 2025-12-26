#!/usr/bin/env python3
# author: deadc0de6

"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2019, deadc0de6
i3wm efficient screen real estate
"""

import sys
import os
import logging
import i3ipc  # pylint: disable=E0401
from docopt import docopt  # pylint: disable=E0401


NAME = 'i3altlayout'
VERSION = '1.1.4'
logger = logging.getLogger(__name__)
USAGE = f"""
{NAME}

Usage:
    {NAME} [-d] [--pid=<path>] [--socket=<path>]
    {NAME} --help
    {NAME} --version

Options:
    -d --debug          Enable debug logs.
    -p --pid=<path>     Write pid to file.
    -s --socket=<path>  i3 socket path.
    -v --version        Show version.
    -h --help           Show this screen.
"""


def log(string):
    """write logs to stderr"""
    logger.debug(string)


def on_window_focus(i3vm, _event):
    """split depending on window size"""
    window = i3vm.get_tree().find_focused()
    log(f'new focused window: {window}')
    if not window:
        return
    if not window.rect:
        return
    if window.layout in ['stacked', 'tabbed']:
        return
    log('is a valid window')

    height = window.rect.height
    width = window.rect.width
    log(f'height: {height}, width: {width}')

    # aspect ratio rule BUT always split vertical if the screen is portrait.
    # Rationale: it's uncommon to have applications that
    #            work well on very tiny width
    workspace_height = window.workspace().rect.height
    workspace_width = window.workspace().rect.width
    if workspace_height > workspace_width:
        layout = 'vertical'
    else:
        if height > width:
            layout = 'vertical'
        else:
            layout = 'horizontal'

    cmd = f'split {layout}'
    log(f'running command: {cmd}')
    i3vm.command(cmd)
    log('\n')


def write_pid(path):
    """write our pid to file"""
    if not path:
        return
    pid = str(os.getpid())
    with open(path, 'w', encoding='utf-8') as file:
        file.write(pid)


def main(spath, ppath):
    """entry point"""
    write_pid(ppath)

    try:
        i3vm = i3ipc.Connection(socket_path=spath)
    except Exception as exc:  # pylint: disable=W0718,W0703
        print(exc)
        return False
    i3vm.on('window::focus', on_window_focus)
    try:
        i3vm.main()
    except KeyboardInterrupt:
        pass
    return True


if __name__ == "__main__":
    def cli():
        """command-line entry point"""
        args = docopt(USAGE, version=VERSION)
        if args['--debug']:
            logging.basicConfig(level=logging.DEBUG)
            logger.setLevel(logging.DEBUG)
        socket_path = args['--socket']
        pid_path = args['--pid']
        if main(socket_path, pid_path):
            sys.exit(0)
        sys.exit(1)

    cli()
