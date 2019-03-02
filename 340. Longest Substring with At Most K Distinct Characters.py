class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        

    if not s or k == 0:
            return 0
        res = 1
        used = dict()
        j = 0
        for i in range(len(s)):
            used[s[i]] = i
            if len(used) == k + 1:
                del_id = min(used.values())
                del used[s[del_id]]
                j = del_id + 1
            res = max(res, i - j + 1)
        return res


if __name__ == "__main__":
    s = "aa"
    k = 1
    print(Solution().lengthOfLongestSubstringKDistinct(s, k))
