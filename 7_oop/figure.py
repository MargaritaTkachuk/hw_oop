import math

class Figure:
    # def __init__(self):
    #     self.self = self

    def dimention(self):
        pass

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        pass



class Triangle(Figure):
    def check_triangle_existence(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __init__(self, a, b, c):
        assert self.check_triangle_existence(a, b, c), "None"
        self.a = a
        self.b = b
        self.c = c

    def dimention(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        half_p = self.perimeter() / 2
        return math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))

    def volume(self):
        return self.square()



class Rectangle(Figure):
    def check_rectangle_existence(self, a, b):
        return a > 0 and b > 0

    def __init__(self, a, b):
        assert self.check_rectangle_existence(a, b), "None"
        self.a = a
        self.b = b

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()



class Trapeze(Figure):
    def check_trapeze_existence(self, a, b, c, d):
        return a > 0 and b > 0 and c > 0 and d > 0 and a != b

    def __init__(self, a, b, c, d):
        assert self.check_trapeze_existence(a, b, c, d), "None"
        self.a = min(a, b)  # Робимо так, щоб a була меншою основою
        self.b = max(a, b)  # b - більшою основою
        self.c = c
        self.d = d

    def dimention(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        p = self.perimeter() / 2
        discriminant = (p - self.a) * (p - self.b) * (p - self.b - self.c) * (p - self.b - self.d)

        if discriminant < 0:
            return 0

        h = (2 / abs(self.b - self.a)) * math.sqrt(discriminant)
        return (self.a + self.b) * h / 2

    def volume(self):
        return self.square()



class Parallelogram(Figure):
    def check_parallelogram_existence(self, a, b, h):
        return a > 0 and b > 0 and h > 0 and h <= max(a, b)

    def __init__(self, a, b, h):
        assert self.check_parallelogram_existence(a, b, h), "None"
        self.a = a
        self.b = b
        self.h = h

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()



class Circle(Figure):
    def check_circle_existence(self, r):
        return r > 0

    def __init__(self, r):
        assert self.check_circle_existence(r), "None"
        self.r = r

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def volume(self):
        return self.square()



class Ball:
    def check_ball_existence(self, r):
        return r > 0

    def __init__(self, r):
        assert self.check_ball_existence(r), "None"
        self.r = r

    def dimention(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * self.r**2

    def squareBase(self):
        return math.pi * self.r**2

    def height(self):
        return 2 * self.r

    def volume(self):
        return 4 * self.r**3 * math.pi / 3



class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimention(self):
        return 3

    def squareSurface(self):
        return 1.5 * self.a * math.sqrt(self.h**2 + (self.a * math.sqrt(3) / 6)**2)

    def squareBase(self):
        return self.a**2 * math.sqrt(3) / 4

    def height(self):
        return self.h

    def volume(self):
        return self.squareBase() * self.h / 3


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return 3

    def squareSurface(self):
        return self.a * math.sqrt(self.h**2 + self.b**2 / 4) + self.b * math.sqrt(self.h**2 + self.a**2 / 4)

    def squareBase(self):
        return self.square()

    def height(self):
        return self.h

    def volume(self):
        return self.squareBase() * self.h / 3
