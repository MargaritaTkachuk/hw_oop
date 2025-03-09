import math

class Triangle:
    def check_triangle_existence(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __init__(self, a, b, c):
        assert self.check_triangle_existence(a, b, c), "None"
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        half_p = self.perimeter() / 2
        return math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))


class Rectangle:
    def check_rectangle_existence(self, a, b):
        return a > 0 and b > 0

    def __init__(self, a, b):
        assert self.check_rectangle_existence(a, b), "None"
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b


class Trapeze:
    def check_trapeze_existence(self, a, b, c, d):
        return a > 0 and b > 0 and c > 0 and d > 0 and a != b

    def __init__(self, a, b, c, d):
        assert self.check_trapeze_existence(a, b, c, d), "None"
        self.a = min(a, b)  # Робимо так, щоб a була меншою основою
        self.b = max(a, b)  # b - більшою основою
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        p = self.perimeter() / 2
        discriminant = (p - self.a) * (p - self.b) * (p - self.b - self.c) * (p - self.b - self.d)

        if discriminant < 0:
            return 0

        h = (2 / abs(self.b - self.a)) * math.sqrt(discriminant)
        return (self.a + self.b) * h / 2


class Parallelogram:
    def check_parallelogram_existence(self, a, b, h):
        return a > 0 and b > 0 and h > 0 and h <= max(a, b)

    def __init__(self, a, b, h):
        assert self.check_parallelogram_existence(a, b, h), "None"
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h


class Circle:
    def check_circle_existence(self, r):
        return r > 0

    def __init__(self, r):
        assert self.check_circle_existence(r), "None"
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

def parse_figure(line):
    parts = line.split()
    name = parts[0]
    params = list(map(int, parts[1:]))
    return name, params

def read_figures_from_file(filename):
    figures = []
    with open(filename, 'r') as file:
        for line in file:
            name, params = parse_figure(line)
            try:
                if name == "Rectangle" and len(params) == 2:
                    figures.append(Rectangle(*params))
                elif name == "Triangle" and len(params) == 3:
                    figures.append(Triangle(*params))
                elif name == "Trapeze" and len(params) == 4:
                    figures.append(Trapeze(*params))
                elif name == "Parallelogram" and len(params) == 3:
                    figures.append(Parallelogram(*params))
                elif name == "Circle" and len(params) == 1:
                    figures.append(Circle(*params))
            except AssertionError:
                continue
    return figures

def find_max_figure(figures, key_func):
    return max(figures, key=key_func, default=None)




if __name__ == '__main__':
    figures = read_figures_from_file('input01.txt')

    max_square_figure = find_max_figure(figures, lambda f: f.square())
    max_perimeter_figure = find_max_figure(figures, lambda f: f.perimeter())

    with open('output.txt', 'w') as f:
        print("Фігура з найбільшою площею:", max_square_figure.__class__.__name__, "Площа:", max_square_figure.square(), file=f)
        print("Фігура з найбільшим периметром:", max_perimeter_figure.__class__.__name__, "Периметр:", max_perimeter_figure.perimeter(), file=f)