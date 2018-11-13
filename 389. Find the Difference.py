class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) > len(t):
                    return s[i]
                else:
                    return t[i]
        if len(s) > len(t):
            return s[-1]
        else:
            return t[-1]

        # ans = 0
        # for c in s + t:
        #     ans ^= ord(c)
        # return chr(ans)


if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t))
