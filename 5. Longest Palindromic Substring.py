class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return
        res = []
        for i in range(len(s)):
            curr = self.dp(s, i, i)
            if curr and len(curr) > len(res):
                res = curr
            curr = self.dp(s, i, i + 1)
            if curr and len(curr) > len(res):
                res = curr
        return res

    def dp(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))
