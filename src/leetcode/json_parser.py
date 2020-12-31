#!/usr/bin/env python3
'JsonParser'

__author__ = "lizhipei"

class JsonFormatException(Exception):
    __name__ = "JsonFormatException"
    

def jsonStringToDic(jsonStr:str):
    stack = list()
    count = 0;
    if len(jsonStr)==0:
        return dict()
    if jsonStr[0] != '[' and jsonStr[0] !='{':
        raise JsonFormatException("json format invalid")
    for i in jsonStr:
        if i=='{':
            stack.append(i)
        if i=='}':
            if stack.pop()=='{':
                count+=1
            else:
                stack.append('{')
    jsonMap = dict()
    return jsonMap

try:
    jsonStringToDic("1")
except Exception as e:
    print(e)