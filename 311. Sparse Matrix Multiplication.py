class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A[0])
        m = len(B)
        if not A or not B or m != n:
            return None
        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            if A[i]:
                for k in range(n):
                    for j in range(len(B[0])):
                        res[i][j] += A[i][k] * B[k][j]
        return res


if __name__ == "__main__":
    A = [[1, -5]]

    B = [[12], [-1]]
    print(Solution().multiply(A, B))
