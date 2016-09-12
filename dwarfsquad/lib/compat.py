from __future__ import print_function


def print_func(arg):
    print_function(arg)


def join_dicts(arg, base):
    try:
        z = arg.copy()
        z.update(base)
        return z
    except SyntaxError:
        return dict(base.items() + arg.items())
