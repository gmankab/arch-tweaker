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
run = subprocess.getstatusoutput

tweaker_dir = os.getcwd()

gmankab_github_io_dir = Path(
    f'{tweaker_dir}/../gmankab.github.io'
).resolve()

tweaker_github_io_dir = f'{gmankab_github_io_dir}/arch'
backup_dir = f'{gmankab_github_io_dir}/backup'

files_list = run(
    'git ls-tree -r main --name-only'
)[1].split('\n')

ban_list = [
    'readme.md',
    '.gitignore',
    'start.sh',
    'links_updater.py',
    'links_updater.sh',
]

for file in ban_list:
    while file in files_list:
        files_list.remove(file)

for file in files_list.copy():
    if file[:4] == 'svg/':
        files_list.remove(file)

print(run(f'rm -r {backup_dir}'))
os.rename(tweaker_github_io_dir, backup_dir)

for filename in files_list:
    file = f'{tweaker_github_io_dir}/{filename}'
    Path(file).parent.mkdir(
        exist_ok=True,
        parents=True,
    )

    file_content = f'<meta http-equiv="refresh" content="1;url=https://raw.githubusercontent.com/gmankab/gmankab.github.io/main/{filename}"/>'
    command = f"echo '{file_content}' > '{file}'"
    print(
        run(
            command
        )
    )

os.system('python ~/proj/init/python/gp.py main')
os.chdir(gmankab_github_io_dir)
os.system('python ~/proj/init/python/gp.py main')