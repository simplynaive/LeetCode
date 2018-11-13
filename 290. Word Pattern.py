class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        d = dict()
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if str[i] in d.values():
                    return False
                d[pattern[i]] = str[i]
            else:
                if d[pattern[i]] != str[i]:
                    return False
        return True


if __name__ == "__main__":
    pattern = "abba"
    str = "dog dog dog dog"
    print(Solution().wordPattern(pattern, str))
