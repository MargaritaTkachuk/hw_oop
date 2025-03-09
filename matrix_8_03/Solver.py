from Matrix2D import Matrix2D
from Vector2D import Vector2D


class Solver:
    def __init__(self, matrix, vector):
        self._matrix = Matrix2D(matrix)
        self._vector = Vector2D(vector)

    def cramer(self):
        det_main = self._matrix.det()
        if self._matrix.check_det():
            matrix_1 = Matrix2D([[self._vector.vector[0], self._matrix.matrix[0][1]],
                                 [self._vector.vector[1], self._matrix.matrix[1][1]]])

            matrix_2 = Matrix2D([[self._matrix.matrix[0][0], self._vector.vector[0]],
                                 [self._matrix.matrix[1][0], self._vector.vector[1]]])

            det_1 = matrix_1.det()
            det_2 = matrix_2.det()

            x1 = det_1 / det_main
            x2 = det_2 / det_main
            return x1, x2

        else:
            return None

if __name__ == '__main__':
    test = Solver([[1, -2], [3, -4]], [1, 7])
    print(test.cramer())