class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True
        flag = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i >= 1 and j >= 1:
                    print(i, j)
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
                    flag = True
        return flag


if __name__ == "__main__":
    matrix = [[18], [66]]
    print(Solution().isToeplitzMatrix(matrix))
