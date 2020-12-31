#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO
import os

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

fio = StringIO()
fio.write('hello')
fio.write(' ')
fio.write('world!')
fio.seek(0)
fio.write('what?')
print('writable=' + str(fio.writable()))
print('readable=' + str(fio.readable()))
print('read=' + fio.read())
print('getValue=' + fio.getvalue())

bio = BytesIO()
bio.write('hello what?'.encode())
print(bio.getvalue())

print('os name = ' + os.name)  # windows系统是nt，linux、unix、Mac OS X 是posix

try:
    # uname函数在windows系统上面不提供。
    print('uname=' + os.uname())
except Exception as e:
    print(e)

print('environ = ' + str(os.environ))  # 输出系统的环境变量
print('environ JAVA_HOME=' + str(os.environ.get('JAVA_HOME')))  # 获取某个环境变量的值

print('abspath=' + os.path.abspath('..'))  # 获取目录的绝对路径
# path = os.path.join('..', 'assets')  # 拼接路径 ，使用此方法来正确处理不同操作系统的路径分隔符
path = os.path.abspath('write.txt')
try:
    os.rmdir(path)  # 删除给定目录(当目录不存在时，无法删除给定目录)
except IOError as ioe:
    print('can`t remove dir')
    print(ioe)
else:
    print('remove dir success')

try:
    os.mkdir(path)  # 创建新目录(当目录存在时，无法创建目录)
except IOError as ioe:
    print('can`t create dir')
    print(ioe)
else:
    print('create dir success')

print('split=' + str(os.path.split(path)))  # 将路径分割为路径和最末端的目录或者文件
print('splitext=' + str(os.path.splitext(path)))  # 从路径中分割路径和文件扩展名，路径末端不是文件时，扩展名获取为空
# os.remove('write.text')
# os.remove('write.t')
# os.rename(path, 'write.t')  # 重命名

listDir = [x for x in os.listdir('../') if not os.path.isdir(x)]  # 当前路径目录列表
for l in listDir:
    print(l)


# 读取指定目录下的所有目录和文件列表，并保存到dirs.txt文件下面
def readDir(path, input_stream, div='    '):
    list_dir = os.listdir(path)
    for d in list_dir:
        print(div + d)
        input_stream.write(div + d + '\n')
        if os.path.isdir(os.path.join(path, d)):
            try:
                readDir(os.path.join(path, d), input_stream, div + '    ')
            except PermissionError as e:
                print('no permission to read path = ' + d)
            finally:
                pass


print('printDir--------------------------------')
# printDir('/')

with open('dirs.txt', 'w') as read_stream:
    readDir('.', read_stream)
