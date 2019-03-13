class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        res = []
        i = 0
        flag = [0] * len(s)
        while i < len(s):
            for word in dict:
                if s[i:i + len(word)] == word:
                    flag[i:i + len(word)] = [1] * len(word)
            i += 1
        i = 0
        while i < len(flag):
            if i == 0 or flag[i - 1] == 0:
                if flag[i] == 1:
                    res.append('<b>')
            res.append(s[i])
            if i == len(flag) - 1 or flag[i + 1] == 0:
                if flag[i] == 1:
                    res.append('</b>')
            i += 1
        return ''.join(res)


if __name__ == "__main__":
    s = "aaabbcc"
    dict = ["aaa", "aab", "bc"]
    print(Solution().addBoldTag(s, dict))
