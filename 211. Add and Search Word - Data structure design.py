class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['#'] = '#'

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        t = self.trie

        def find(t, word):
            # print(word)
            if not word:
                return '#' in t
            c, word = word[0], word[1:]
            if c != '.':
                return c in t and find(t[c], word)
            else:
                print(t)
                for v in t.values():
                    print(v, t, word)
                    if find(v, word):
                        return True
            return True

        return find(t, word)


if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("a")
    obj.addWord("a")
    print(obj.search("."))
    print(obj.search("a"))  #false
    print(obj.search("aa"))  #true
    print(obj.search(".a"))  #true
    print(obj.search("a."))  #true
