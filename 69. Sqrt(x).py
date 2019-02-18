class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        i = 0
        if x > 0:
            while i * i <= x:
                i += 1
        return i - 1


if __name__ == "__main__":
    x = 212121
    print(Solution().mySqrt(x))
