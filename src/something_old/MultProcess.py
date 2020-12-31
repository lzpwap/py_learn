#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from multiprocessing import Process

print('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
print('process (%s) start...' % os.getpid())

# only works on Unix/Linux/Mac
try:
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s)' % (os.getpid(), pid))
except Exception as e:
    pass


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    # p = Process(target=run_proc, args=('child_1',))
    p = Process()
    if p == 0:
        print('this is child process')
    else:
        print('create child process %s' % p.pid)
    print('child process will start')
    p.start()
    print('pid=%s' % str(p.pid))
    p.join()
    print('child process end')
else:
    print('I (%s) am child process' % os.getpid())
    print('parent is %s' % os.getppid())

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')



