class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s):
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    ns = s[:x] + s[x + 1:]
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans

        def calc(s):
            a = b = 0
            for c in s:
                if c == '(':
                    a += 1
                elif c == ')':
                    a -= 1
                if a < 0:
                    b += 1
                a = max(a, 0)
            return a + b

        visited = {s}
        return dfs(s)

    #     # return one solution
    #     left = right = 0
    #     i = 0
    #     l = len(s)
    #     while i < l:
    #         if s[i] == '(':
    #             left += 1
    #         elif s[i] == ')':
    #             if right < left:
    #                 right += 1
    #             else:
    #                 s = s[:i] + s[i + 1:]
    #                 i -= 1
    #                 l -= 1
    #                 if self.validate(s):
    #                     return s
    #                 else:
    #                     self.removeInvalidParentheses(s)
    #         i += 1
    #     if self.validate(s):
    #         return s
    #     return ''
    #
    # def validate(self, s):
    #     left = right = 0
    #     for i in range(len(s)):
    #         if s[i] == '(':
    #             left += 1
    #         elif s[i] == ')':
    #             if right < left:
    #                 right += 1
    #             else:
    #                 return False
    #     return True


if __name__ == "__main__":
    s = '(a)()))('
    print(Solution().removeInvalidParentheses(s))
