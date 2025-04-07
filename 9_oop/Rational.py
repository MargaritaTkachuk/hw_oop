from math import gcd
import copy

class Rational:
    def __init__(self, n: (int, str), d = 1):
        if isinstance(n, Rational):
            self._n = n._n
            self._d = n._d
        else:
            if isinstance(n, str):
                n, d = map(int, n.split('/'))
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

    def __call__(self):
        return f'{(self._n / self._d):.2f}'

    def __getitem__(self, item):
        if item == 'n':
            return self._n
        elif item == 'd':
            return self._d
        else:
            return None

    def __setitem__(self, item, value):
        if item == 'n':
            self._n = value
        elif item == 'd':
            self._d = value
        self._n = self._n // gcd(self._n, self._d)
        self._d = self._d // gcd(self._n, self._d)


if __name__ == '__main__':
    res = Rational(2, 3) + Rational(5) * Rational(5, 6)
    res2 = Rational(2, 3) * 5
    print(res2)
    res2['n'] = 1
    # print(res2.__setitem__('n', 4))
    print(res2)
    rat = Rational('3/9')
    rat1 = copy.copy(rat)
    print(rat)
    print(rat1)