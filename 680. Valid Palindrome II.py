class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = -1, len(s)

        def valid(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while i < j:
            i += 1
            j -= 1
            if s[i] != s[j]:
                return valid(i + 1, j) or valid(i, j - 1)
        return True


if __name__ == "__main__":
    s = "cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu"
    print(Solution().validPalindrome(s))
