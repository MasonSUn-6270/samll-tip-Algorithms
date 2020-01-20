import itertools

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


def check_24(**kwargs):
    for i in kwargs.values():
        if eval(i) == 24:
            print(i)


for card_ in cards_iter():
    for symbol_ in symbol_iter():
        check_24(
            ev1=' {0}{4} {1} {5} {2} {6} {3}  '.format(*card_, *symbol_),
            ev2=' ({0}{4} {1}) {5} {2} {6} {3}  '.format(*card_, *symbol_),
            ev3=' (({0}{4} {1}) {5} {2}) {6} {3}  '.format(*card_, *symbol_),
        )
