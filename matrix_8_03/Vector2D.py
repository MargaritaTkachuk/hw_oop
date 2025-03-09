class Vector2D:
    def __init__(self, vector = [1, 0]):
        self.vector = vector

    def input_file(self, row):
        a, b = map(int, row.split())
        self.vector[0] = a
        self.vector[1] = b

    def output_show(self):
        print(*self.vector)

    # def output_file(self, filename):
    #     with open(filename, 'w') as f:
    #         print(*self.vector, file=f)

if __name__ == '__main__':
    vector22 = Vector2D([33, 66])
    Vector2D.output_show(vector22)
    with open('rhs_values.txt', 'r') as f:
        for row in f:
            try:
                vec = Vector2D()
                Vector2D.input_file(vec, row)
                Vector2D.output_show(vec)

            except ValueError:
                continue