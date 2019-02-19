class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            i = (n - 1) % 26
            n = (n - 1) // 26
            res = ''.join((chr(i + ord('A')), res))
        return res


if __name__ == "__main__":
    n = 28
    print(Solution().convertToTitle(n))
