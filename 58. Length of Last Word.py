class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s.split(' ')
        while len(s) > 0 and not s[-1]:
            s = s[:-1]
        if len(s) == 0:
            return 0
        return len(s[-1])


if __name__ == "__main__":
    s = "a "
    print(Solution().lengthOfLastWord(s))
