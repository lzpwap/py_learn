#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a md5 module"""

__author__ = 'lzzzp'  # 可以被直接引用的变量
_me = 'i am '  # 不可被直接引用的private变量

import sys


def _main():  # 不可被直接引用的private方法
    print('main private method')


def get_md5(s):
    return 'this is md5 str=' + s


def test():
    args = sys.argv
    print('init ', get_md5('hello'))
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello , %s' % args[1])
    else:
        print('to many arguments')


if __name__ == '__main__':
    test()
