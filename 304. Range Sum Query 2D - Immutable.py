class NumMatrix(object):
    # caching on row
    # def __init__(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     """
    #     self.matrix = []
    #     for r in range(len(matrix)):
    #         if r + 1 > len(self.matrix):
    #             self.matrix.append([matrix[r][0]])
    #         for c in range(1, len(matrix[0])):
    #             self.matrix[r].append(self.matrix[r][c - 1] + matrix[r][c])
    #
    # def sumRegion(self, row1, col1, row2, col2):
    #     """
    #     :type row1: int
    #     :type col1: int
    #     :type row2: int
    #     :type col2: int
    #     :rtype: int
    #     """
    #     s = 0
    #     for r in range(row1, row2 + 1):
    #         if col1 >= 1:
    #             s += self.matrix[r][col2] - self.matrix[r][col1 - 1]
    #         else:
    #             s += self.matrix[r][col2]
    #     return s


    # All caching

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            matrix = [[0]]
        self.matrix = [[0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        for r in range(1, len(matrix) + 1):
            for c in range(1, len(matrix[0]) + 1):
                self.matrix[r][c] = self.matrix[r][c - 1] + self.matrix[r - 1][c] + matrix[r - 1][c - 1] - \
                                    self.matrix[r - 1][c - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.matrix[row2 + 1][col2 + 1] - self.matrix[row1][col2 + 1] - self.matrix[row2 + 1][col1] + \
               self.matrix[row1][col1]


if __name__ == "__main__":
    matrix = [[-1]]
    row1, col1, row2, col2 = 0, 0, 0, 0
    print(NumMatrix(matrix).sumRegion(row1, col1, row2, col2))