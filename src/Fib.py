#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


class Fib(object):
    def __init__(self, name=''):
        self.name = name
        self.a, self.b = 0, 1
        self.path = name

    def __str__(self):  # print(Fib('lzp')) __str__()
        return self.path

    __repr__ = __str__

    def __iter__(self):  # 表明类的实例是一个可迭代的对象,需要同时声明__next__来迭代实例
        return self

    def __next__(self):  # 迭代时，调用__next__来产生斐波那契数列
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):  # __getitem__方法用于根据下标区数据，也可以根据slice取范围的数据
        a, b = 1, 1
        if isinstance(item, int):
            for n in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start, stop = item.start, item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l
        return a

    def __getattr__(self, item):  # 当尝试调用实例的某个属性并且属性不存在时，会尝试调用此方法
        return Fib(str('%s/%s' % (self.path, item)))

    def __call__(self, *args, **kwargs):  # 实现此方法，就可以将对象实例当成方法来进行调用。
        print('call Fib name=' + self.name)


f = Fib('lzp')
print(f.__repr__)  # print __str__()

for i in f:
    print(i)

print('index f=' + str(f[100]))
print('slice f=' + str(f[1:4]))
print(f.age)
print(Fib().age.sex.student.height.width)

print(callable(f))

f()

Month = Enum('MM', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month.Feb.value)

print('weekday----------------')


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fir = 5
    Sat = 6


print(Weekday.Sun)
print(Weekday(1))
for name, member in Weekday.__members__.items():
    print(name, '=>', member)
