class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_list = [0] * 26
        p_list = [0] * 26
        n = len(p)
        res = []
        for c in p:
            p_list[ord(c) - ord('a')] += 1
        for i in range(len(s)):
            s_list[ord(s[i]) - ord('a')] += 1
            if i >= n:
                s_list[ord(s[i - n]) - ord('a')] -= 1
            if s_list == p_list:
                res.append(i - n + 1)
        return res


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))
