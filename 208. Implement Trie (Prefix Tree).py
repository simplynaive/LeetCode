class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            print('aaaaaa', t)
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.trie)
    print(trie.search("apple"))  # returns true
    print(trie.search("app"))  # returns false
    print(trie.startsWith("app"))  # returns true
    trie.insert("app")
    print(trie.trie)
    print(trie.search("app"))  # returns true

