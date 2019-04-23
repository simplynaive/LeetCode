class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dic = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                pre = word[:i]
                suf = word[i:]

                if pre in dic and suf in dic:
                    return True
                if pre in dic and dfs(suf):
                    return True
                if suf in dic and dfs(pre):
                    return True

            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res


if __name__ == "__main__":
    # words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    words = ['highway', 'high', 'way', 'superhero', 'super', 'hero']
    print(Solution().findAllConcatenatedWordsInADict(words))
