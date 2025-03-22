import math

class Figure:
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
        assert self.check_triangle_existence(a, b, c), "Triangle with these sides cannot exist"
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        assert self.check_triangle_existence(a, self.__b, self.__c), "Invalid value for a"
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        assert self.check_triangle_existence(self.__a, b, self.__c), "Invalid value for b"
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        assert self.check_triangle_existence(self.__a, self.__b, c), "Invalid value for c"
        self.__c = c

    def dimention(self):
        return 2

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def square(self):
        half_p = self.perimeter() / 2
        return math.sqrt(half_p * (half_p - self.__a) * (half_p - self.__b) * (half_p - self.__c))

    def volume(self):
        return self.square()



class Rectangle(Figure):
    def check_rectangle_existence(self, a, b):
        return a > 0 and b > 0

    def __init__(self, a, b):
        assert self.check_rectangle_existence(a, b), "Rectangle with these sides cannot exist"
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        assert self.check_rectangle_existence(a, self.__b), "Invalid value for a"
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        assert self.check_rectangle_existence(self.__a, b), "Invalid value for b"
        self.__b = b

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * (self.__a + self.__b)

    def square(self):
        return self.__a * self.__b

    def volume(self):
        return self.square()



class Trapeze(Figure):
    def check_trapeze_existence(self, a, b, c, d):
        return a > 0 and b > 0 and c > 0 and d > 0 and a != b

    def __init__(self, a, b, c, d):
        assert self.check_trapeze_existence(a, b, c, d), "Trapeze with these sides cannot exist"
        self.__a = min(a, b)
        self.__b = max(a, b)
        self.__c = c
        self.__d = d

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        assert self.check_trapeze_existence(a, self.__b, self.__c, self.__d), "Invalid value for a"
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        assert self.check_trapeze_existence(self.__a, b, self.__c, self.__d), "Invalid value for b"
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        assert self.check_trapeze_existence(self.__a, self.__b, c, self.__d), "Invalid value for c"
        self.__c = c

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, d):
        assert self.check_trapeze_existence(self.__a, self.__b, self.__c, d), "Invalid value for d"
        self.__d = d

    def dimention(self):
        return 2

    def perimeter(self):
        return self.__a + self.__b + self.__c + self.__d

    def square(self):
        p = self.perimeter() / 2
        discriminant = (p - self.__a) * (p - self.__b) * (p - self.__b - self.__c) * (p - self.__b - self.__d)

        if discriminant < 0:
            return 0

        h = (2 / abs(self.__b - self.__a)) * math.sqrt(discriminant)
        return (self.__a + self.__b) * h / 2

    def volume(self):
        return self.square()



class Parallelogram(Figure):
    def check_parallelogram_existence(self, a, b, h):
        return a > 0 and b > 0 and h > 0 and h <= max(a, b)

    def __init__(self, a, b, h):
        assert self.check_parallelogram_existence(a, b, h), "Parallelogram with these parameters cannot exist"
        self.__a = a
        self.__b = b
        self.__h = h

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        assert self.check_parallelogram_existence(a, self.__b, self.__h), "Invalid value for a"
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        assert self.check_parallelogram_existence(self.__a, b, self.__h), "Invalid value for b"
        self.__b = b

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        assert self.check_parallelogram_existence(self.__a, self.__b, h), "Invalid value for h"
        self.__h = h

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * (self.__a + self.__b)

    def square(self):
        return self.__a * self.__h

    def volume(self):
        return self.square()



class Circle(Figure):
    def check_circle_existence(self, r):
        return r > 0

    def __init__(self, r):
        assert self.check_circle_existence(r), "Circle with this radius cannot exist"
        self.__r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        assert self.check_circle_existence(r), "Invalid value for r"
        self.__r = r

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.__r

    def square(self):
        return math.pi * self.__r ** 2

    def volume(self):
        return self.square()



class Ball(Figure):
    def check_ball_existence(self, r):
        return r > 0

    def __init__(self, r):
        assert self.check_ball_existence(r), "Ball with this radius cannot exist"
        self.__r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        assert self.check_ball_existence(r), "Invalid value for r"
        self.__r = r

    def perimetr(self):
        return None

    def square(self):
        return None

    def dimention(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * self.__r**2

    def squareBase(self):
        return math.pi * self.__r**2

    def height(self):
        return 2 * self.__r

    def volume(self):
        return 4 * self.__r**3 * math.pi / 3



class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.__h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        assert h > 0, "Invalid value for h"
        self.__h = h

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 1.5 * self.a * math.sqrt(self.__h**2 + (self.a * math.sqrt(3) / 6)**2)

    def squareBase(self):
        return self.a**2 * math.sqrt(3) / 4

    def height(self):
        return self.__h

    def volume(self):
        return self.squareBase() * self.__h / 3



class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.__h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        assert h > 0, "Invalid value for h"
        self.__h = h

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return self.a * math.sqrt(self.__h**2 + self.b**2 / 4) + self.b * math.sqrt(self.__h**2 + self.a**2 / 4)

    def squareBase(self):
        return self.a * self.b

    def height(self):
        return self.__h

    def volume(self):
        return self.squareBase() * self.__h / 3



class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.__c = c

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        assert c > 0, "Invalid value for c"
        self.__c = c

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 2 * self.__c * (self.a + self.b)

    def squareBase(self):
        return self.a * self.b

    def height(self):
        return self.__c

    def volume(self):
        return self.a * self.b * self.__c



class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.__h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        assert h > 0, "Invalid value for h"
        self.__h = h

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return math.pi * self.r * math.sqrt(self.r**2 + self.__h**2)

    def squareBase(self):
        return math.pi * self.r**2

    def height(self):
        return self.__h

    def volume(self):
        return self.squareBase() * self.__h / 3



class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.__h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        assert h > 0, "Invalid value for h"
        self.__h = h

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return self.__h * (self.a + self.b + self.c)

    def squareBase(self):
        half_p = self.perimeter() / 2
        return math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))

    def height(self):
        return self.__h

    def volume(self):
        return self.squareBase() * self.__h