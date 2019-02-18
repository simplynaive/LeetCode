class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n < 3:
            return pow(k, n)
        same = k
        diff = k * (k - 1)
        for i in range(3, n + 1):
            t = same
            same = diff
            diff = (t + diff) * (k - 1)
        return same + diff


if __name__ == "__main__":
    n = 3
    k = 2
    print(Solution().numWays(n, k))
