"""
Compile this project as a mcpack.
"""

import shutil
import glob
import os
import commentjson

NAME = 'Assets Plus'

def main():
    # Setup dist from src
    shutil.copytree("src", "dist", dirs_exist_ok=True)

    # Get version
    with open('src/manifest.json', 'r') as fd:
        manifest = commentjson.load(fd)
        version = '.'.join([str(x) for x in manifest['header']['version']])

    # Copy files
    shutil.copy('LICENSE', 'dist/LICENSE')
    shutil.copy('CHANGELOG.md', 'dist/CHANGELOG.md')

    # Minify all JSON
    for file in glob.glob('dist/**/*.json',recursive=True):
        if os.path.isfile(file):
            with open(file, 'r') as fd:
                data = commentjson.load(fd)

            string = commentjson.dumps(data, separators=(',', ':'))
            with open(file, 'w') as fd:
                fd.write(string)

    # Archive dist
    fp = f'libs/{ NAME } { version }'
    shutil.make_archive(fp, 'zip', 'dist')
    os.rename(fp+'.zip', fp+'.mcpack')

if __name__ == '__main__':
    main()
