from figure import *

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
                elif name == "Ball" and len(params) == 1:
                    figures.append(Ball(*params))
                elif name == "TriangularPyramid" and len(params) == 2:
                    figures.append(TriangularPyramid(*params))
                elif name == "QuadrangularPyramid" and len(params) == 3:
                    figures.append(QuadrangularPyramid(*params))
                elif name == "RectangularParallelepiped" and len(params) == 3:
                    figures.append(RectangularParallelepiped(*params))
                elif name == "Cone" and len(params) == 2:
                    figures.append(Cone(*params))
                elif name == "TriangularPrism" and len(params) == 4:
                    figures.append(TriangularPrism(*params))
            except AssertionError:
                continue
    return figures

def find_max_figure(figures, key_func):
    return max(figures, key=key_func, default=None)


####################### main prog ###########################

if __name__ == '__main__':
    figures = read_figures_from_file('input01 (2).txt')

    max_volume_figure = find_max_figure(figures, lambda f: f.volume())

    with open('output.txt', 'w') as f:
        print("Figure with max volume:", max_volume_figure.__class__.__name__, file=f)
        print("Volume:", max_volume_figure.volume(), file=f)
