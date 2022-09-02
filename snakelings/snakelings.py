"""CLI interface for snakelings."""
# standard library
import json
import os
from pathlib import Path
import sys

# third-party
import appdirs
import click

# first-party

def _gen_default_config():
    return {
        'snakelings_version': '0.1.0',
        'project_version': None,
        'project_directory': None,
    }

def _get_config_file_path():
    """Return path to the config file, creating necessary directory structure as needed."""
    config_file_dir_path = Path(appdirs.user_config_dir(appname='charmer', appauthor='cblades'))
    os.makedirs(config_file_dir_path, exist_ok=True)
    return config_file_dir_path/'config.json'

@click.command()
def main():
    """Simple program that greets NAME for a total of COUNT times."""
    config_file_dir_path = Path(appdirs.user_config_dir(appname='charmer', appauthor='cblades'))
    os.makedirs(config_file_dir_path, exist_ok=True)
    config_file_path = config_file_dir_path/'config.json'

    if config_file_path.exists():
        with open(config_file_path, 'r', encoding='utf-8') as config_file:
            try:
                config = json.load(config_file)
            except json.JSONDecodeError:
                print(f'Configuration file at...\n\n\t{config_file_path}\n'
                      f'\n...is invalid and can not be read.  Delete file to re-generate.')
                sys.exit(1)
    else:
        config_file_path.touch()
        with open(config_file_path, 'w', encoding='utf-8') as config_file:
            

            config_file.write(_gen_default_config())


if __name__ == '__main__':
    main()
