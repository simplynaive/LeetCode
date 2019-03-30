class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if not word or not abbr:
            return False
        num = 0
        i, j = 0, 0
        while j < len(abbr):
            if abbr[j].isalpha():
                i += num
                num = 0
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                if str(num) == abbr[j] == '0':
                    return False
                num = num * 10 + int(abbr[j])
                j += 1

        return i + num == len(word) and j == len(abbr)


if __name__ == "__main__":
    s = "internationalization"
    abbr = "i5a11o1"
    print(Solution().validWordAbbreviation(s, abbr))
