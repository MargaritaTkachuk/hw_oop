from math import gcd
import copy

class Rational:
    def __init__(self, n, d = 1):
        if isinstance(n, Rational):
            self._n = n._n
            self._d = n._d
        else:
            assert self.is_exist(n, d)
            self._n = n // gcd(n, d)
            self._d = d // gcd(n, d)

    def is_exist(self, n, d):
        return d != 0

    def __str__(self):
        return f'{self._n}/{self._d}'

    def __add__(self, other: ('Rational', int)):
        if isinstance(other, int):
            d = self._d
            n = self._n + self._d * other
        else:
            d = self._d * other._d
            n = self._n * other._d + self._d * other._n
        return Rational(n, d)

    def __mul__(self, other: ('Rational', int)):
        if isinstance(other, int):
            d = self._d
            n = self._n * other
        else:
            d = self._d * other._d
            n = self._n * other._n
        return Rational(n, d)


if __name__ == '__main__':
    res = Rational(2, 3) + Rational(5) * Rational(5, 6)
    res2 = Rational(2, 3) * 5
    print(res2)
    # rat = Rational(3, 18)
    # rat1 = copy.copy(rat)
    # print(rat)
    # print(rat1)