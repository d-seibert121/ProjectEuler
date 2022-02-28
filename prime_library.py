from sympy.ntheory import Sieve, prime, factorint, multiplicity
from collections import Counter
from functools import reduce
import operator


class Factors(Counter):
    def product(self: Counter):
        return reduce(operator.mul, self.elements(), 1)


def factor(n: int) -> Factors:
    return Factors(factorint(n))
