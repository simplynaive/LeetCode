class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)
        length = 0
        for i in range(len(s)):
            existed = [s[i]]
            for j in range(i + 1, len(s)):
                if s[j] in existed:
                    length = max(length, j - i)
                    break
                else:
                    existed.append(s[j])
                length = max(length, len(existed))
        return length


if __name__ == "__main__":
    s = "au"
    print(Solution().lengthOfLongestSubstring(s))