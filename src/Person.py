#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Person Class"""
from types import MethodType
import random


# 类和实例
class Person(object):  # 继承于object的Person类
    __slots__ = ('sex', 'height', '_age', '_name')

    def __init__(self, age, name):
        self._age = age
        self._name = name

    def setName(self, name):
        self._name = name

    def setAge(self, age):
        self._age = age

    def getName(self):
        return 'his name is ' + str(self._name) + ' and his age is ' + str(self._age)


lzzzp = Person(23, 'john')
maaa = Person(12, 'kotlin')

lzzzp.setAge(50)
print(lzzzp.getName())
print(maaa.getName())


class Animal(object):
    name = 4
    sex = 'man'

    def __len__(self):
        return 10

    def __init__(self, name):
        self.name = name

    def jump(self):
        print('height = ' + str(int(random.random() * 100)))

    def eat(self, food):
        print('eating ' + str(food))


class Tomcat(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + ' is eating ' + str(food))


animal = Animal('animal')
animal.jump()
animal.eat('fish')

tomcat = Tomcat('tomcat')
tomcat.jump()
tomcat.eat('fish')

print(isinstance(tomcat, Tomcat))
print(isinstance(tomcat, Animal))
print(type(tomcat))
print(type(animal))
print(dir(animal))

print(len(animal))

print(hasattr(tomcat, 'eat'))
print(hasattr(tomcat, 'play'))
print(getattr(tomcat, 'name'))
print(getattr(tomcat, 'age', None))

print('isInstance=' + str(isinstance(tomcat, (Person or animal))))
print('isInstance=' + str(isinstance((tomcat, animal), list)))
print('isInstance=' + str(isinstance((tomcat, animal), tuple)))
print('isInstance=' + str(isinstance([tomcat, animal], (list, tuple))))

print(animal.name)
print(Animal.name)
Animal.name = 10
print(tomcat.name)
print(Tomcat.name)


def set_sex(self, sex):
    self.sex = sex


s = Animal('jump duck')
i = Animal('jump cat')
Animal.set_sex = MethodType(set_sex, s)
s.set_sex('woman')
i.set_sex('man')
print(s.name + ' is a ' + s.sex)
print(i.name + ' is a ' + i.sex)


