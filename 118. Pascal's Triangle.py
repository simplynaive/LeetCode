class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows or numRows < 1:
            return []
        res = []

        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, row_num):
                row[j] = res[row_num - 1][j - 1] + res[row_num - 1][j]

            res.append(row)

        return res


if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))
# Input: 5
# Output:
# [
#  [1],
#  [1,1],
#  [1,2,1],
#  [1,3,3,1],
#  [1,4,6,4,1]
# ]
