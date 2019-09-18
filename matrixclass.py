import copy
class MyMatrix:
    def __init__(self, data: list):
        self.matrix = copy.deepcopy(data)
        self.width = 0
        self.height = 0

    def __repr__(self):
        s = ''
        for line in self.matrix:
            s += '\n'
            for i in range(len(self.matrix[0])):
                    s += str(line[i]) + ' '
        return s[1::]


    def size(self) -> tuple:
        self.height = len(self.matrix)
        self.weight = len(self.matrix[0])
        s = (self.height, self.weight)
        return s

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
        flipped_matrix = copy.deepcopy(self.matrix)
        return flipped_matrix[::-1]

    def flipped_left_right(self):
        flipped_matrix = []
        for row in self.matrix:
            flipped_matrix.append(row[::-1])
        return flipped_matrix

    def transpose(self):
        self.matrix = [[row[i] for row in self.matrix] for i in range(len(self.matrix[0]))]
        return self.matrix

    def transposed(self):
        self.matrix_copy = copy.deepcopy(self.matrix)
        self.matrix_copy = [[row[i] for row in self.matrix_copy] for i in range(len(self.matrix[0]))]
        return self.matrix_copy
