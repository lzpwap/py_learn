#!/usr/bin/env python3
'JsonParser'

__author__ = "lizhipei"


class JsonFormatException(Exception):
    __name__ = "JsonFormatException"


class Symbol():
    __slots__ = ("_symbol", "_index")

    def __init__(self, symbol, index) -> None:
        self.setSymbol(symbol)
        self.setIndex(index)

    def setSymbol(self, value):
        self._symbol = value

    def getSymbol(self):
        return self._symbol

    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self._index

    def isObjEnd(self):
        return self._symbol == '}'

    def isObjStart(self):
        return self._symbol == '{'

    def isArrStart(self):
        return self._symbol == '['

    def isArrEnd(self):
        return self._symbol == ']'


def isObjEnd(c: str):
    return c == '}'


def isObjStart(c: str):
    return c == '{'


def isArrStart(c: str):
    return c == '['


def isArrEnd(c: str):
    return c == ']'


def jsonStringToDic(jsonStr: str):
    if len(jsonStr) == 0:
        return dict()
    if not isObjStart(jsonStr[0]) and not isArrStart(jsonStr[0]):
        raise JsonFormatException("json format invalid")

    stack = list()
    index = 0
    while index < len(jsonStr):
        char = jsonStr[index]
        if isObjStart(char):
            stack.append(Symbol(char, index))
        if isArrStart(char):
            stack.append(Symbol(char, index))
        index += 1
    jsonMap = dict()
    return jsonMap


def parseObj(obj: str):
    return dict()


def nextObjectStartSymbol(currIndex, jsonStr: str):
    index = currIndex+1
    while index < len(jsonStr):
        if isObjEnd(jsonStr[index]):
            return index
        index += 1
    return -1


try:
    jsonStringToDic("1")
except Exception as e:
    print(e)
