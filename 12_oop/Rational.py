from math import gcd
from RationalError import *

class Rational:
    def __init__(self, n: (int, str), d=1):
        if isinstance(n, Rational):
            self._n = n._n
            self._d = n._d
        else:
            if isinstance(n, str):
                try:
                    n, d = map(int, n.split('/'))
                except Exception:
                    raise RationalValueError("String format must be 'numerator/denominator'")
            if d == 0:
                raise RationalError()
            common = gcd(n, d)
            self._n = n // common
            self._d = d // common

    def __str__(self):
        return f'{self._n}/{self._d}'

    def __add__(self, other):
        if not isinstance(other, (int, Rational)):
            raise RationalValueError()
        if isinstance(other, int):
            other = Rational(other)
        d = self._d * other._d
        n = self._n * other._d + self._d * other._n
        return Rational(n, d)

    def __sub__(self, other):
        if not isinstance(other, (int, Rational)):
            raise RationalValueError()
        if isinstance(other, int):
            other = Rational(other)
        d = self._d * other._d
        n = self._n * other._d - self._d * other._n
        return Rational(n, d)

    def __mul__(self, other):
        if not isinstance(other, (int, Rational)):
            raise RationalValueError()
        if isinstance(other, int):
            other = Rational(other)
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
            if value == 0:
                raise RationalError()
            self._d = value
        common = gcd(self._n, self._d)
        self._n = self._n // common
        self._d = self._d // common



if __name__ == '__main__':
    # res = Rational(2, 3) - Rational(5) * Rational(5, 6)
    # res2 = Rational(2, 3) * 5
    # print(res)
    # res2['n'] = 1
    # # print(res2.__setitem__('n', 4))
    # print(res2)
    # rat = Rational('3/9')
    # rat1 = copy.copy(rat)
    # print(rat)
    # print(rat1)
    line = '73  -  90  -  25  -  33/22  +  11/40  -  64/19  -  23/91  -  48  *  92  +  53'
    lst = line.split()
    print(lst)
    list_rational = []
    list_operators = []

    for el in lst:
        if el in '-+*':
            list_operators.append(el)
        else: list_rational.append(el)

    for i in range(len(list_rational)):
        try: list_rational[i] = int(list_rational[i])
        except ValueError:
            continue

    print(list_rational)
    print(list_operators)


    mult = []
    for i in range(len(list_operators)):
        if list_operators[i] == '*':
            mult.append(i)


    print(mult)

    for index in mult:
        mult_num = Rational(list_rational[index]) * Rational(list_rational[index + 1])
        list_rational[index: index + 2] = [str(mult_num)]
        list_operators.pop(index)

    print(list_rational)
    print(list_operators)

    res = Rational(list_rational[0])
    for rational, operator in zip(list_rational[1:], list_operators):
        num = Rational(rational)
        if operator == '-':
            res -= num
        elif operator == '+':
            res += num

    print(res())
