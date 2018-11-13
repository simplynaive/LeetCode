class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
        res = []
        for word in words:
            if len(word) == 1:
                res.append(word)
            else:
                for l in line:
                    if word[0].lower() in l:
                        for i in range(1, len(word)):
                            if word[i].lower() not in l:
                                break
                            if i == len(word) - 1:
                                res.append(word)
        return res


if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(Solution().findWords(words))
