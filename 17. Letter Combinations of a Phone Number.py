class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        def dfs(combination, next_digit):
            if len(next_digit) == 0:
                res.append(combination)

            else:
                for c in dic[next_digit[0]]:
                    dfs(combination + c, next_digit[1:])

        res = []
        if digits:
            dfs("", digits)

        return res


if __name__ == "__main__":
    digits = '332'
    print(Solution().letterCombinations(digits))
