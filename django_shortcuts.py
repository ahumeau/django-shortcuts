#!/usr/bin/env python

import os
import sys
from subprocess import call

ALIASES = {
    # Django
    'c'  : 'collectstatic',
    'r'  : 'runserver',
    'sd' : 'syncdb',
    'sp' : 'startproject',
    'sa' : 'startapp',
    't'  : 'test',
    
    # Shell
    'd'  : 'dbshell',
    's'  : 'shell',
    
    # Auth
    'csu': 'createsuperuser',
    'cpw': 'changepassword',
    
    # South
    'm'  : 'migrate',
    'sm' : 'schemamigration',
    
    # Haystack
    'ix' : 'update_index',
    'rix': 'rebuild_index',
    
    # Django Extensions
    'sk' : 'generate_secret_key',
    'rdb': 'reset_db',
    'rp' : 'runserver_plus',
    'shp': 'shell_plus',
    'url': 'show_urls',
    'gm' : 'graph_models',
    'rs' : 'runscript'
}

def run(command=None, *arguments):
    """
    Run the given command.

    Parameters:
    :param command: A string describing a command.
    :param arguments: A list of strings describing arguments to the command.
    """

    if command == 'startproject' or ALIASES[command] == 'startproject':
        return call('django-admin.py startproject %s' % ' '.join(arguments), shell=True)

    if command and command in ALIASES:
        command = ALIASES[command]

    script_path = os.getcwd().split(os.sep)
    while not os.path.exists('/%s/manage.py' % os.sep.join(script_path)):
        try:
            script_path.pop()
        except IndexError:
            sys.exit('django-shortcuts: No \'manage.py\' script found in this directory or its parents.')

    call('%(python)s %(script_path)s %(command)s %(arguments)s' % {
        'python': sys.executable,
        'script_path': '/%s/manage.py' % os.path.join(*script_path),
        'command': command or '',
        'arguments': ' '.join(arguments)
    }, shell=True)


def main():
    """Entry-point function."""
    run(*sys.argv[1:])

if __name__ == '__main__':
    main()