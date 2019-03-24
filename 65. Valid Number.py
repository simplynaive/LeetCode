class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        s = s.strip()
        res = sign = e = dot = False
        i = 0
        while i < len(s):
            if s[i].isdigit():
                res = sign = True
            elif s[i] == '.' and not dot:
                dot = sign = True
            elif s[i] in 'eE' and not e and res:
                dot = e = True
                res = sign = False
            elif s[i] in '+-' and not res and not sign:
                sign = True
            else:
                return False
            i += 1
        return res


if __name__ == "__main__":
    s = "0.1"
    print(Solution().isNumber(s))
