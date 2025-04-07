from Rational import Rational

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

if __name__ == '__main__':
    lst = RationalList([1, '1/2', 'hui', 1.33, 12])
    lst0= '3/33'
    lst += lst0
    print(lst)


