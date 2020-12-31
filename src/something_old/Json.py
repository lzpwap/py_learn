#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import pickle

d = dict(name='Bob', age=20, score=99)
print('d = ' + str(d))
seri = pickle.dumps(d)
print('d = ' + str(type(seri)))

with open('dump.txt', 'wb') as dump_f:
    pickle.dump(d, dump_f)

with open('dump.txt', 'rb') as dump_f:
    d = pickle.load(dump_f)
    print('read dump.txt = ' + str(d))

with open('dump.json', 'w') as dump_f:
    json.dump(d, dump_f)

with open('dump.json', 'r') as dump_f:
    print('read dump.json = ' + str(json.load(dump_f)))


class JsonObject(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def getObjectDict(self, *args, **kw):
        return {
            'name': self.name,
            'age': self.age,
            'score': self.score
        }


def jsonObject2dict(obj):
    return {
        'name': obj.name,
        'age': obj.age,
        'score': obj.score
    }


jo = JsonObject('lzp', 20, 88)
jo_json = json.dumps(jo, default=jo.getObjectDict)
jo_json_1 = json.dumps(jo, default=lambda obj: obj.__dict__)
print('jo_json = ' + str(jo_json))
print('jo_json_1 = ' + str(jo_json_1))
print('jo.__dict__ = ' + str(jo.__dict__))
