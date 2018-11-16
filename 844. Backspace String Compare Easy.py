class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if self.backspace(S) == self.backspace(T):
            return True
        return False

    def backspace(self, str):
        res = []
        for c in str:
            if c != '#':
                res.append(c)
            else:
                res = res[:-1]
        return res


if __name__ == "__main__":
    S = "ab#c"
    T = "ad#c"
    print(Solution().backspaceCompare(S, T))
