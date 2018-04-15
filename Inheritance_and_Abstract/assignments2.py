import abc
from datetime import datetime

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self, filename):
        return

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()

class LogFile(WriteFile):

    def write(self, msg):
        dt = datetime.now()
        dt_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0} {1}'.format(dt_str, msg))

class DelimFile(WriteFile):

    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, msg):
        line = self.delim.join(msg)
        self.write_line(line)