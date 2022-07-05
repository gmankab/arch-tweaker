#!/bin/python

'''
this creates files for repo https://github.com/gmankab/gmankab.github.io/arch, wich will redirecting user to https://github.com/gmankab/arch-tweaker
'''

import os
import subprocess
from pathlib import Path
from rich import pretty
from rich.console import Console

pretty.install()

console = Console()

print = console.print

tweaker_dir = os.getcwd()
gmankab_github_io_dir = Path(
    f'{tweaker_dir}/../gmankab.github.io'
).resolve()

output = subprocess.getstatusoutput(
    'git ls-tree -r main --name-only'
)[1]

print(output.split('\n'))

