import time


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0:
            return False
        for i in range(len(matrix)):
            if len(matrix) == 1:
                for m in matrix[i]:
                    if m == target:
                        return True
                return False
            elif i == len(matrix) - 1:
                for m in matrix[-1]:
                    if m == target:
                        return True
                return False
            elif matrix[i + 1][0] > target:
                for m in matrix[i]:
                    if m == target:
                        return True
                return False
        return False


if __name__ == "__main__":
    matrix = [[1], [3]]
    target = 3

    start = time.time()
    solution = Solution()
    print(solution.searchMatrix(matrix, target))
    end = time.time()
    print("runtime = ", end - start)
