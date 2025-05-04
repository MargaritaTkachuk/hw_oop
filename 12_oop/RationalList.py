from Rational import Rational, RationalValueError

class RationalList:
    def __init__(self, data=None):
        self.data = []
        if data is not None:
            for el in data:
                try:
                    self.data.append(Rational(el))
                except (ValueError, TypeError):
                    raise RationalValueError(f"Invalid element '{el}' in initialization list")

    def __str__(self):
        return str([str(el) for el in self.data])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        try:
            self.data[key] = Rational(value)
        except (ValueError, TypeError):
            raise RationalValueError(f"Invalid value '{value}' for Rational assignment")

    def __add__(self, other):
        new_data = self.data.copy()
        if isinstance(other, RationalList):
            new_data += other.data
        elif isinstance(other, (Rational, int, str)):
            try:
                new_data.append(Rational(other))
            except (ValueError, TypeError):
                raise RationalValueError(f"Cannot add invalid value '{other}' to RationalList")
        else:
            raise RationalValueError(f"Unsupported operand type '{type(other)}' for addition")
        return RationalList(new_data)

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data += other.data
        elif isinstance(other, (Rational, int, str)):
            try:
                self.data.append(Rational(other))
            except (ValueError, TypeError):
                raise RationalValueError(f"Cannot add invalid value '{other}' to RationalList")
        else:
            raise RationalValueError(f"Unsupported operand type '{type(other)}' for in-place addition")
        return self

    def to_sun_rationals(self):
        result = Rational(0)
        for el in self.data:
            result += el
        return result



if __name__ == '__main__':
    lst = RationalList([1, '1/2', 1.33, 12])
    lst0= '1/0'
    lst += lst0
    print(lst)


