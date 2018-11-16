class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        s = list(s)
        for i in range(len(s) // 2):
            t = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = t
        return "".join(s)

        # return s[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().reverseString(s))
