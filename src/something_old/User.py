#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Field(object):
    def __init__(self, name, cloumn_type):
        self.name = name
        self.cloumn_type = cloumn_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


def printStr(*arg, **kw):
    print('printStr ' + 'arg=' + str(arg) + ' kw=' + str(kw))


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model:%s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        attrs['print'] = printStr
        attrs['hello'] = 'Hello world!'
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("'" + str(getattr(self, k)) + "'")
            args.append(getattr(self, k))
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL : %s' % sql)
        print('ARGS : %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
u.print()
print(u.hello)

try:
    a = 10 / 0
except BaseException as e:
    print(e)
finally:
    print('finally ')
