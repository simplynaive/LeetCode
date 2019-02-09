class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i + 1:]
                    if tmp not in visited and tmp in wordList:
                        queue.append((tmp, dist + 1))
                        visited.add(tmp)
        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
