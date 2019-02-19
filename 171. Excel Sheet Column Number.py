class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        for a in s:
            res = 26 * res + (ord(a) - ord('A') + 1)
        return res


if __name__ == "__main__":
    s = 'AB'
    print(Solution().titleToNumber(s))
