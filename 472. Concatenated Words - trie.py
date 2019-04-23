class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.tail = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.tail = True

    def hasConcat(self, word, index, wordcount):
        node = self.root
        n = len(word)
        for i in range(index, n):
            c = word[i]
            if c not in node.children:
                return False
            if node.children[c].tail:
                if i == n - 1:
                    return wordcount >= 1
                if self.hasConcat(word, i + 1, wordcount + 1):
                    return True
            node = node.children[c]
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        trie = Trie()
        res = []
        for word in words:
            if len(word):
                trie.addWord(word)
        for word in words:
            if len(word):
                if trie.hasConcat(word, 0, 0):
                    res.append(word)
        return res


if __name__ == "__main__":
    # words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    words = ['highway', 'high', 'way', 'superhero', 'super', 'hero']
    print(Solution().findAllConcatenatedWordsInADict(words))
