class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        import numpy as np
        if not matrix or not matrix[0]:
            return []
        matrix = np.array(matrix)
        upper = left = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        res = []
        while left < right and upper < down:
            res.extend(matrix[upper, left:right])
            res.extend(matrix[upper:down, right])
            res.extend(matrix[down, left + 1:right + 1][::-1])
            res.extend(matrix[upper + 1:down + 1, left][::-1])

            left += 1
            right -= 1
            upper += 1
            down -= 1
        matrix = list(matrix)
        if left == right:
            for i in range(upper, down + 1):
                res.extend([matrix[i][left]])
        elif upper == down:
            for j in range(left, right + 1):
                res.extend([matrix[upper][j]])

        return res


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().spiralOrder(matrix))
