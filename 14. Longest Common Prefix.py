class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]

        shortest = min(strs,  key=len)
        for i in range(len(shortest)):
            for str in strs:
                if str[i] != shortest[i]:
                    if i > 0:
                        return shortest[:i]
                    else:
                        return ""
        return shortest


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
