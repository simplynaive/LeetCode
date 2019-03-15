class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # # TLE
        # res = []
        # A = sorted([x for x in s1])
        # B = [x for x in s2]
        # n = len(s1)
        # for i in range(len(B) - n + 1):
        #     print(sorted(B[i:i+n]), A)
        #     if sorted(B[i:i+n]) == A:
        #         res.append(i)
        # return res

        res = []
        s1_list = [0]*26
        s2_list = [0]*26
        for s in s1:
            s1_list[ord(s) - ord('a')] += 1

        for i, s in enumerate(s2):
            s2_list[ord(s) - ord('a')] += 1
            if i >= len(s1):
                s2_list[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if s1_list == s2_list:
                res.append(i - len(s1) + 1)
        return res


if __name__ == "__main__":
    s1 = "abcd"
    s2 = 'bacdgabcda'
    print(Solution().checkInclusion(s1, s2))
