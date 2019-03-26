class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = 0
        s = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp += 1
                s += dp
            else:
                dp = 0
        return s


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    print(Solution().numberOfArithmeticSlices(A))
