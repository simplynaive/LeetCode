class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d = sorted(d)
        d.sort(key=len, reverse=True)
        for word in d:
            j = 0
            for i in range(len(s)):
                if s[i] == word[j]:
                    if j == len(word) - 1:
                        return word
                    j += 1
        return ""


if __name__ == "__main__":
    s = "aewfafwafjlwajflwajflwafj"
    d = ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]
    print(Solution().findLongestWord(s, d))
