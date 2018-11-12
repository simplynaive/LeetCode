class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()
        for i in s:
            d[i] = d.get(i, 0) + 1
        for j in t:
            if j not in d:
                return False
            else:
                d[j] -= 1
        return all(x == 0 for x in d.values())

        # if len(s) != len(t):
        #     return False
        # s = sorted(s)
        # t = sorted(t)
        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         return False
        # return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
