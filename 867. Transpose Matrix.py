class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        line_len = len(A[0])
        column_len = len(A)
        for i in range(line_len):
            res.append([])
            for j in range(column_len):
                res[i].append(A[j][i])
        return res


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    print(Solution().transpose(A))
