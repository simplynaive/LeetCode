class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if stack == [] or left[right.index(c)] != stack.pop():
                    return False
            else:
                return False
        return stack == []


if __name__ == "__main__":
    s = "()[]{}"
    print(Solution().isValid(s))
