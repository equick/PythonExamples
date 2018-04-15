import os

class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as fh:
                for line in fh:
                    configval = line.rstrip()
                    key, val = configval.split('=', 1)
                    dict.__setitem__(self, key, val)


    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            for key, val in self.items():
                fh.write('{0}={1}\n'.format(key, val))