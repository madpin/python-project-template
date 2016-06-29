# -​*- coding: utf-8 -*​-


def sum(a, b, c=[0]):
    return reduce(lambda x, y: x+y, c, a+b)


def sub(a, b):
    return a - b
