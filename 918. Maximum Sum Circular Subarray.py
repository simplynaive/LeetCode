class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if max(A) < 0:
            return max(A)
        minSum = A[:]
        maxSum = A[:]
        for i in range(1, len(A)):
            if maxSum[i - 1] > 0:
                maxSum[i] += maxSum[i - 1]
            if minSum[i - 1] < 0:
                minSum[i] += minSum[i - 1]
        return max(max(maxSum), sum(A) - min(minSum))


if __name__ == "__main__":
    A = [1, 2, 3]
    print(Solution().maxSubarraySumCircular(A))
