from functools import reduce
from typing import Optional, Iterable


class Calc:
    def __init__(self, ext_obj=None):
        if ext_obj:
            # print('Connecting...')
            self.external_object = ext_obj
            self.external_object.connect()
            # print('End connection...')

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'inf'

    def avg(self,
            iterable: Iterable,
            upper: Optional[int] = None,
            lower: Optional[int] = None) -> float:
        if upper:
            iterable = list(filter(lambda x: x < upper, iterable))
        if lower:
            iterable = list(filter(lambda x: x > lower, iterable))
        if len(iterable) == 0:
            return 0
        return sum(iterable) / len(iterable)
