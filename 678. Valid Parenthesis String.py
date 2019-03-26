class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        left = 0
        star = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                left -= 1
            if c != ')':
                star += 1
            else:
                star -= 1

            if star < 0:
                break
            left = max(left, 0)
        return left == 0


if __name__ == "__main__":
    s = "((*)"
    print(Solution().checkValidString(s))
