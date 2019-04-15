class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        extra_right = []
        a = b = 0
        for i, c in enumerate(s):
            if c == '(':
                a += 1
            elif c == ')':
                a -= 1
            if a < 0:
                b += 1
                extra_right.append(i)
            a = max(a, 0)
        for i in range(len(s) - 1, 0, -1):
            if i in extra_right or (a > 0 and s[i] == '('):
                s = s[:i] + s[i + 1:]
                a -= 1
        return s


if __name__ == "__main__":
    s = '(a)()))()('
    print(Solution().removeInvalidParentheses(s))
