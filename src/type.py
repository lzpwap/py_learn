import math
from functools import reduce

import functools

from src.util.utils import get_md5

a = 123


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def move(mx, my, step, angle=0):
    nx = mx + step * math.cos(angle)
    ny = my + step * math.sin(angle)
    return nx, ny


print(my_abs(-12))

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
nl = ['0', '1', 2, '3', 4, (5.1, 5.2, 5.3)]
nl.insert(nl.__sizeof__(), '6')
for i in nl:
    print(type(i))
    if isinstance(i, tuple):
        for j in i:
            print(j)
    else:
        print(i)


def power(px, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * px
    return s


print(power(10, 4))

pwd = '123456'
print(get_md5(pwd))


def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


num = [1, 2, 3]
print(calc(*num))


def person(name, age, *args, **kw):
    print('name=', name)
    print('age=', age)
    if 'sex' in kw:
        print('sex=', kw['sex'])
        pass
    if 'height' in kw:
        print('height=', kw['height'])
        pass
    if 'width' in kw:
        print('height=', kw['width'])
        pass
    for arg in args:
        print(arg)


extra = {'sex': 'man', 'height': '1.7m'}
args = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
person('lzzzp', 25, *args, **extra)
print('slice=', args[2:4])

l1 = [x * x for x in range(1, 11)]
print(l1)
l2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l2)
l3 = [(m + n.lower()) for m in 'ABC' for n in 'XYZ']
print(l3)
l4 = (n for n in range(1, 100))  # 生成器 generator


# generator
# num need >0
def oddGen(num):
    n = 0
    for m in range(0, num):
        n = n + m
        yield n
    return


for num in oddGen(10):
    print(num)


# Iterator  迭代器 (生成器对象) .next

# Iterable  可迭代对象 (数据集合对象)


def abs_add(x, y, fun):
    return fun(x) + fun(y)


print('abs_add=', abs_add(-10, 9, abs))

l5 = map(abs, [1, -2, 3, -4, 5, -6, -7, 8, -9])

for i in l5:
    print(i)


def add(x, y):
    return x * 10 + y


l6 = reduce(add, [1, 3, 5, 7, 5, 5, 6, 8, 9])
print(l6)
l7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, l7)))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# TODO  what is lambda
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 10:
        print(n)
    else:
        break
print('-------------------------------------------------------------------------------------------')


def returnSun():
    fs = []

    def f(n):
        def g():
            return n * n

        return g

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = returnSun()

print(f1())
print(f2())
print(f3())


def createCounter():
    i = 0

    def counter():
        nonlocal i
        i = i + 1
        return i

    return counter


f4 = createCounter()

print(f4())
print(f4())
print(f4())

print((lambda x: x * x)(4))


def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        print('params %s , %s' % (args, kw))
        result = func(*args, **kw)
        print(func.__name__ + '()' + ',result=%s' % result)
        return result

    return wrapper


def logMsg(text):
    def dec(func):
        def wrapper(*args, **kw):
            print(text)
            print('call %s()' % func.__name__)
            print('params %s , %s' % (args, kw))
            result = func(*args, **kw)
            print(func.__name__ + '()' + ',result=%s' % result)
            return result

        return wrapper

    return dec


@logMsg('this is now')
def now(num, **kw):
    if num > 200:
        print('num>200')
    else:
        print('num<200')
    return '2018-06-30'


@logMsg('this is when')
def when(num, **kw):
    if num > 200:
        print('num>200')
    else:
        print('num<200')
    return '2018-06-30'


print(now(150, **{'sex': 'women'}))
print(when(150, **{'sex': 'man'}))

print(int('100'))
int2 = functools.partial(int, base=2)
print(int2('100'))

