class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for c in S:
            l = []
            for i in res:
                if c.isdigit():
                    l.append(str(i) + str(c))
                else:
                    l.append(str(i) + str(c).lower())
                    l.append(str(i) + str(c).upper())
            res = l
        return res


if __name__ == "__main__":
    S = "a1b2"
    print(Solution().letterCasePermutation(S))

