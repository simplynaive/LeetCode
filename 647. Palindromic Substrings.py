class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res


if __name__ == "__main__":
    s = 'aaaa'
    print(Solution().countSubstrings(s))
