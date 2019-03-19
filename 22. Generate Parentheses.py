class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # res = []
        #
        # def backtrack(s='', left=0, right=0):
        #     if len(s) == 2 * n:
        #         res.append(s)
        #         return res
        #     if left < n:
        #         backtrack(s + '(', left + 1, right)
        #     if right < n:
        #         backtrack(s + ')', left, right + 1)
        # backtrack()
        # return res

        res = []

        def generate(l, r, s):
            if len(s) == 2 * n:
                res.append(s)
                return res
            if r <= l < n:
                generate(l + 1, r, s + '(')
            if r < n:
                generate(l, r + 1, s + ')')

        generate(0, 0, '')
        return res


if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))
