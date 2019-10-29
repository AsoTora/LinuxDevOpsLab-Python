# Andrei Shveday

import platform
import sys
import os
import pkg_resources
from distutils.sysconfig import get_python_lib
import json
import random
import string


'''
ments.
'''


def get_info():
    info = {}

    info['python version'] = platform.python_version()
    info['python exec'] = sys.executable

    try:
        info['virtualenv'] = os.environ['VIRTUAL_ENV']
    except KeyError:
        info['virtualenv'] = None

    info['pip'] = get_python_lib() + '/pip'

    try:
        info['pythonpath'] = os.environ['PYTHONPATH']
    except KeyError:
        info['pythonpath'] = None

    packages = {}
    for p in pkg_resources.working_set:
        packages[p.project_name] = p.version
    info['installed packages'] = packages

    info['site-packages location'] = get_python_lib()

    write_json(info)

    try:
        import yaml
        with open('data.yaml', 'w') as f:
            yaml.dump(info, f)
    except ImportError:
        print('yaml is not supported in this env!')


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def write_json(info):
    list = {}

    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            list = json.load(f)
    with open('data.json', 'w') as f:
        '''
         I'm not sure about this moment. I use it for optional task and dumping dict of dicts.
        Otherwise I get non-json format {},{} in data.json file
        To use normally for 1 run only:
            json.dump(info, indent=2)
        '''
        list[randomString()] = info
        json.dump(list, f, indent=2)


if __name__ == '__main__':
    get_info()
