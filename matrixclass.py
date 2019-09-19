import copy
class MyMatrix:
    def __init__(self, data: list):
        self.matrix = copy.deepcopy(data)
        self.width = 0
        self.height = 0

    def size(self) -> tuple:
        if self.matrix == []:
            s = (0, 0)
        else:
            self.height = len(self.matrix)
            self.weight = len(self.matrix[0])
            s = (self.height, self.weight)
        return s

    def __repr__(self):
        if (self.size() == (0, 0) or self.size() == (1, 0)):
            return 'Matrix is empty'
        else:
            s = ''
            for line in self.matrix:
                s += '\n'
                for i in range(len(self.matrix[0])):
                        s += str(line[i]) + ' '
            return s[1::]

    def flip_up_down(self):
        self.matrix = self.matrix[::-1]
        return self.matrix

    def flip_left_right(self):
        flipped_matrix = []
        for row in self.matrix:
            flipped_matrix.append(row[::-1])
        self.matrix = copy.deepcopy(flipped_matrix)
        return self.matrix

    def flipped_up_down(self):
        flipped_matrix = MyMatrix(copy.deepcopy(self.matrix))
        return flipped_matrix.flip_up_down()

    def flipped_left_right(self):
        flipped_matrix = MyMatrix(copy.deepcopy(self.matrix))
        flipped_matrix = flipped_matrix.flip_left_right()
        return flipped_matrix

    def transpose(self):
        self.matrix = [[row[i] for row in self.matrix] for i in range(len(self.matrix[0]))]
        return self.matrix

    def transposed(self):
        flipped_matrix = MyMatrix(copy.deepcopy(self.matrix))
        flipped_matrix = flipped_matrix.transpose()
        return flipped_matrix
