import copy
class MyMatrix:
    def __init__(self, data: list):
        self.matrix = copy.deepcopy(data)

    def size(self) -> tuple:
        if self.matrix == []:
            s = (0, 0)
        else:
            height = len(self.matrix)
            weight = len(self.matrix[0])
            s = (height, weight)
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

    """def __get_data(self, nowlist):
        for i in range (int(self.size()[0])):
            rowList = []
            for j in range (int(self.size()[1])):
                if nowlist[j] not in matrix:
                    rowList.append(nowlist[j])
        matrix.append(rowList)
        return matrix"""

    def flip_up_down(self):
        self.matrix = self.matrix[::-1]
        return self

    def flip_left_right(self):
        flipped_matrix = []
        for row in self.matrix:
            flipped_matrix.append(row[::-1])
        self.matrix = copy.deepcopy(flipped_matrix)
        return self

    def flipped_up_down(self):
        flipped_matrix = MyMatrix(self.matrix)
        flipped_matrix.flip_up_down()
        return flipped_matrix.matrix

    def flipped_left_right(self):
        flipped_matrix = MyMatrix(self.matrix)
        flipped_matrix = flipped_matrix.flip_left_right()
        return flipped_matrix.matrix

    def transpose(self):
        self.matrix = [[row[i] for row in self.matrix] for i in range(len(self.matrix[0]))]
        return self

    def transposed(self):
        flipped_matrix = MyMatrix(self.matrix)
        flipped_matrix = flipped_matrix.transpose()
        return flipped_matrix.matrix
