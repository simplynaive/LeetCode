class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1
        if dividend * divisor < 0:
            flag = -1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0

        i = 0
        c = 1
        d = divisor
        while dividend >= divisor:
            if dividend >= d:
                dividend -= d
                i += c
                d += d
                c += c
            else:
                d = (d >> 1)
                c = (c >> 1)

        return min(max(-2147483648, flag * i), 2147483647)


if __name__ == "__main__":
    dividend = 2147483647
    divisor = 3
    print(Solution().divide(dividend, divisor))

