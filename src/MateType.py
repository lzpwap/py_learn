#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class HelloMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class Hello(object, metaclass=HelloMetaclass):
    def hello(self, name='world'):
        print('Hello ,%s' % name)

    def append(self, value):
        print('append value=' + str(value))


Hello().hello()
print(type(Hello))
print(type(Hello()))

h = Hello()
h.add(1)
