"""
Doctests:
>>> seven(times(five()))
35
>>> four(plus(nine()))
13
>>> eight(minus(three()))
5
>>> six(divided_by(two()))
3
"""


def operacao(n, args):
    return {
        '+': n + args[0][0], '-': n - args[0][0], '*': n * args[0][0]
    }.get(args[0][1]) if args[0][1] != '/' else n // args[0][0]


def zero(*args):
    return operacao(0, args) if args else 0


def one(*args):
    return operacao(1, args) if args else 1


def two(*args):
    return operacao(2, args) if args else 2


def three(*args):
    return operacao(3, args) if args else 3


def four(*args):
    return operacao(4, args) if args else 4


def five(*args):
    return operacao(5, args) if args else 5


def six(*args):
    return operacao(6, args) if args else 6


def seven(*args):
    return operacao(7, args) if args else 7


def eight(*args):
    return operacao(8, args) if args else 8


def nine(*args):
    return operacao(9, args) if args else 9


def plus(n):
    return [n, '+']


def minus(n):
    return [n, '-']


def times(n):
    return [n, '*']


def divided_by(n):
    return [n, '/']
