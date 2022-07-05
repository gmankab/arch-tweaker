#!/bin/python

'''
this script copyes files from gmankab/arch-tweaker repo to  gmankab/gmankab.github.io/arch
'''

import os
import subprocess
import shutil
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
if Path(tweaker_github_io_dir).exists():
    os.replace(tweaker_github_io_dir, backup_dir)

exceptions = {
    'tweaks/main': ''
}

for filename in files_list:
    edited_filename = filename
    if filename[:6] == 'tweaks':
        edited_filename = filename[7:]
    folders = [
        f'{tweaker_github_io_dir}/{edited_filename}',
    ]
    for key, val in exceptions.items():
        print(filename)
        if filename == key:
            folders.append(
                f'{tweaker_github_io_dir}/{val}'
            )

    print(folders)
    for folder in folders:
        Path(folder).mkdir(
            exist_ok=True,
            parents=True,
        )

        shutil.copy(
            f'{tweaker_dir}/{filename}',
            f'{folder}/index.html'
        )


os.system('python ~/proj/init/python/gp.py main')
os.chdir(gmankab_github_io_dir)
os.system('python ~/proj/init/python/gp.py main')
