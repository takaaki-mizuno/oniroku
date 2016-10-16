#!/usr/bin/env python

import click
from oniroku import Oniroku
import os


@click.command(help='Oniroku')  # (1)
@click.option('-n', '--name', 'name', type=str, help='project name', required=True)
@click.option('-f', '--file', 'file', type=str, help='project json file name', required=False)
@click.option('-d', '--directory', 'directory', type=str, help='project directory', required=False)
def main(name, file, directory):
    if file is None:
        file = name + '.json'
    if directory is None:
        directory = os.getcwd()

    oniroku = Oniroku(name, file, directory)
    oniroku.execute()


if __name__ == '__main__':
    main()
