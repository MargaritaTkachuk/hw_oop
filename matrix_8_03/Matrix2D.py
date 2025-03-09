class Matrix2D:
    def __init__(self, matrix = [[1, 0], [0, 1]]):
        self.matrix = matrix

    def output_show(self):
        for i in range(2):
            print(*self.matrix[i])

    def output_file(self, filename):
        with open(filename, 'a') as f:
            for i in range(2):
                print(*self.matrix[i], file=f)
            print(file=f)


    def input_keyboard(self):
        a, b, c, d = map(int, input().split())
        self.matrix[0][0] = a
        self.matrix[0][1] = b
        self.matrix[1][0] = c
        self.matrix[1][1] = d

    def input_file(self, row):
        a, b, c, d = map(int, row.split())
        self.matrix[0][0] = a
        self.matrix[0][1] = b
        self.matrix[1][0] = c
        self.matrix[1][1] = d

    def det(self):
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

    def check_det(self):
        if self.det() == 0:
            return False
        else:
            return True

if __name__ == '__main__':
    # test1 = Matrix2D([[2, 3], [6, 3]])
    # Matrix2D.output_show(test1)
    # test = Matrix2D()
    # Matrix2D.output_show(test)
    # Matrix2D.input_keyboard(test)
    # Matrix2D.output_show(test)
    # print(Matrix2D.det(test))
    # print(Matrix2D.check_det(test))
    # Matrix2D.output_file()

    # Matrix2D.show(test)
    # Matrix2D.input_keyboard(test)
    # Matrix2D.show(test)

    with open('matrix_coefficients.txt', 'r') as f:
        for row in f:
            try:
                mat1 = Matrix2D()
                Matrix2D.input_file(mat1, row)
                Matrix2D.output_show(mat1)
                print(mat1.det())
                print()
                # Matrix2D.output_file(mat1,'test_output.txt')
            except ValueError:
                continue




