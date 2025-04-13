from Rational import Rational

class RationalListIterator:
    def __init__(self, data):
        self.sorted_data = sorted(data, key=lambda r: (-r._d, -r._n))
        self.index = 0

    def __next__(self):
        if self.index >= len(self.sorted_data):
            raise StopIteration
        value = self.sorted_data[self.index]
        self.index += 1
        return value


class RationalList:
    def __init__(self, data=None):
        if data is None:
            data = []
            self.data = data
        else:
            self.data = []
            for el in data:
                try:
                    self.data.append(Rational(el))
                except (ValueError, TypeError):
                    continue

    def __str__(self):
        return str([str(el) for el in self.data])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        try:
            self.data[key] = Rational(value)
        except ValueError:
            pass

    def __add__(self, other: ('RationalList', Rational, int)):
        if isinstance(other, RationalList):
            self.data += other.data
        else:
            self.data += [other]
        return RationalList(self.data)

    def __iadd__(self, other: ('RationalList', Rational, int)):
        if isinstance(other, RationalList):
            self.data += other.data
        else:
            self.data += [other]
        return RationalList(self.data)

    def to_sun_rationals(self):
        result = Rational(0)
        for el in self.data:
            result += el
        return result

    def __iter__(self):
        return RationalListIterator(self.data)



if __name__ == '__main__':
    lst = RationalList([1, '1/2', 'hui', 1.33, 12, '5/8', '7/8', '3/4'])
    for r in lst:
        print(r)



