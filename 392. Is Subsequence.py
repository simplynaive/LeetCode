class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1

        return i == len(s)


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))
