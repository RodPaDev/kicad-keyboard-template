from os import path, rename
from posixpath import join
from sys import argv
from pathlib import Path
from posix import listdir

new_name = argv[1]
path = Path.cwd()
files = listdir(path)

prefix = 'Keyboard_Template'

for index, file in enumerate(files):
    if file.startswith(prefix):
        new_file = file.replace(prefix, new_name)
        print(f'{file} -> {new_file}')
        rename(join(path, file), join(path, new_file))
    index += 1
