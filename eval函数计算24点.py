import itertools
import re

"""
def eval(*args, **kwargs): # real signature unknown

    Evaluate the given source in the context of globals and locals.

    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.

    pass
"""

x = 7
print(eval('3 * x'))
symbols = "+-*/"
cards = range(1, 14)


def cards_iter():
    for i in itertools.product(cards, repeat=4):
        yield i


def symbol_iter():
    for i in itertools.product(symbols, repeat=3):
        yield i


for card_ in cards_iter():
    for symbol_ in symbol_iter():
        ev1 = '{0}{4}{1}{5}{2}{6}{3}'.format(*card_, *symbol_)
        ev2, ev3,ev4 = '', '',''
        if '{4}'.format(*card_, *symbol_) in '+-' and '{5}'.format(*card_, *symbol_) in '*/':
            ev2 = '({0}{4}{1}){5}{2}{6}{3}'.format(*card_, *symbol_)
        else:
            ev2 = '0'
        if '{4}'.format(*card_, *symbol_) in '+-' and '{5}'.format(*card_, *symbol_) in '+-'and '{6}'.format(*card_, *symbol_) in '*/':
            ev3 = '({0}{4}{1}{5}{2}){6}{3}'.format(*card_, *symbol_)
        else:
            ev3 = '0'
        if '{4}'.format(*card_, *symbol_) in '+-' and '{5}'.format(*card_, *symbol_) in '*/'and '{6}'.format(*card_, *symbol_) in '+-':
            ev4 = '({0}{4}{1}){5}({2}{6}{3})'.format(*card_, *symbol_)
        else:
            ev4 = '0'
        for i in [ev1, ev2, ev3,ev4]:
            try:
                if eval(i) == 24:
                    print(i)
            except ZeroDivisionError:
                ...