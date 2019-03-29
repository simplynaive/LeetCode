class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0

        while x or y:
            if x % 2 != y % 2:
                res += 1
            x //= 2
            y //= 2

        return res


if __name__ == "__main__":
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
