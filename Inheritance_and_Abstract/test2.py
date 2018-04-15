#!/usr/bin/python

from assignments2 import LogFile, DelimFile

log = LogFile('log.txt')
c = DelimFile('test.csv', ',')

log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])