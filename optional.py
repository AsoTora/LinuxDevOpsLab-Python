import os
import glob
import re

if __name__ == '__main__':
    path = os.environ['HOME'] + "/.pyenv/versions/**/bin/python*"
    envlist = glob.glob(path, recursive=True)
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for env in envlist:
        if re.match('.*python[0-9]$', env):
            os.system('{} "{}/info.py"'.format(env, dir_path))
