class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if not s:
            return ""
        s = list(s)
        v = []
        for i in range(len(s)):
            if s[i] in vowels:
                v.append(s[i])

        for i in range(len(v) // 2):
            t = v[i]
            v[i] = v[len(v) - 1 - i]
            v[len(v) - 1 - i] = t
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = v[j]
                j += 1
        return "".join(s)


if __name__ == "__main__":
    s = "race car"
    print(Solution().reverseVowels(s))
