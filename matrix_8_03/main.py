from Matrix2D import Matrix2D
from Vector2D import Vector2D
from Solver import Solver

with open('matrix_coefficients.txt', 'r') as f1, open('rhs_values.txt', 'r') as f2, open('solutions.txt', 'w') as f3:
    for row in f1:
        matrix = Matrix2D()
        matrix.input_file(row)
        vector = Vector2D()
        vector.input_file(f2.readline())
        solution = Solver(matrix.matrix, vector.vector)
        sols_list = solution.cramer()
        print('Matrix:', file=f3)
        print(*matrix.matrix[0], file=f3)
        print(*matrix.matrix[1], file=f3)
        print('Vector: ', tuple(vector.vector), file=f3)
        print('Solutions: ', sols_list, file=f3)
        print(file=f3)

