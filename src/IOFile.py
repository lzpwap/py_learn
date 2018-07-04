#!/usr/bin/env python3
# -*- coding: utf-8 -*-
f = None
f1 = None
try:
    f = open(r'test.txt', 'r', encoding='utf8')
    # print(f.readline())
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

    f1 = open(r'write.txt', 'a')
    f1.writelines('i am fine!')

except IOError as ioe:
    print(ioe)
finally:
    if f is not None:
        f.close()
        print('file close')
    else:
        print('read error')

    if f1 is not None:
        f1.close()
        print('f1 close')
    else:
        print('write error')

with open('width.txt', 'r') as f2:
    print(f2.read())
    # f2.write('write a text')

print('------------------------')

from io import StringIO
from io import BytesIO

fio = StringIO()
fio.write('hello')
fio.write(' ')
fio.write('world!')
fio.seek(0)
fio.write('what?')
print('read=' + fio.read())
print('getValue=' + fio.getvalue())

bio = BytesIO()
bio.write('hello what?'.encode())
print(bio.getvalue())
