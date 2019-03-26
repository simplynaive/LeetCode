class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1:
            return False
        elif not t and len(s) == 1:
            return True
        elif not s and len(t) == 1:
            return True
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                else:
                    if len(s) > len(t):
                        return t[i:] == s[i + 1:]
                    return s[i:] == t[i + 1:]
        return abs(len(s) - len(t)) == 1


if __name__ == "__main__":
    s = 'a'
    t = 'ac'
    print(Solution().isOneEditDistance(s, t))

