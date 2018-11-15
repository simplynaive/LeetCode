class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for c in s:
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = ""
    print(Solution().firstUniqChar(s))
