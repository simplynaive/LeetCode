class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        res = 1

        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        return res


if __name__ == "__main__":
    x = 2.00000
    n = 10
    print(Solution().myPow(x, n))
