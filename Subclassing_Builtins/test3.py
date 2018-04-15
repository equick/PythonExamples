#!/usr/bin/python

"""
    Usages:
    ./test3.py                        (reads out the entire config file)
    ./test3.py thiskey thisvalue      (sets thiskey and thisvalue in the config file)
"""

import sys
from assignments3 import ConfigDict

cd = ConfigDict('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing date: {0}, {1}'.format(key, value))

    cd[key] = value
else:
    print('reading data')
    for key in cd.keys():
        print('    {0} = {1}'.format(key, cd[key]))