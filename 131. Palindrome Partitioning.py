class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return
        result = []
        self.dfs(s, [], result)
        return result

    def dfs(self, s, string, result):
        print("string:", string)
        if len(s) == 0:
            result.append(list(string))
            return
        for i in range(1, len(s) + 1):
            pre = s[:i]
            print("pre:", pre)
            if pre == pre[::-1]:
                self.dfs(s[i:], string + [pre], result)


if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))
