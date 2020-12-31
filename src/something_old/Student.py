#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Student class"""


class Student(object):
    __slots__ = ('_name', '_age', '_birth', '_score')

    def __init__(self):
        self._score = 0
        self._name = ''
        self._birth = '2018-07-02'

    def getScore(self):
        return self._score

    def setScore(self, value):
        if not isinstance(value, int):
            raise ValueError('score must bet int')
        elif value < 0 or value > 100:
            raise ValueError('score must between 0 to 100')
        else:
            self._score = value

    @property
    def name(self):
        print('name is ' + self._name)
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must bet str')
        else:
            self._name = value

    @property
    def birth(self):
        print('birth is ' + self._birth)
        return self._birth


s1 = Student()

s1.setScore(59)
s1.setScore(100)

s1.name = 'lzzzp'
s1.name

s1.birth


class Screen(object):
    def __init__(self):
        self._width = 0
        self._height = 0
        self._resolution = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError('width must be int')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise ValueError('height must be int')
        else:
            self._height = height

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


class A(object):
    def __init__(self):
        print('A init')

    def foo(self):
        print('A foo')

    def bar(self):
        print('A bar')


class B(object):
    def __init__(self):
        print('B init')

    def foo(self):
        print('B foo')

    def bar(self):
        print('B bar')


class C1(A):
    pass


class C2(B):
    def bar(self):
        print('C2 Bar')


class D(C1, C2):
    pass


class E(A, B):
    pass


if __name__ == '__main__':
    print(D.__mro__)
    d = D()
    d.foo()
    d.bar()

e = E()
