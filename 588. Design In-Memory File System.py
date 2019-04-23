class TrieNode(object):
    def __init__(self):
        self.children = {}

    def setdefault(self, token):
        self.children[token] = TrieNode()
        return self.children[token]

    def get(self, token):
        return self.children.get(token, None)


class FileSystem(object):

    def __init__(self):
        self.root = TrieNode()
        self.fileInfo = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path in self.fileInfo:
            return path.split('/')[-1:]

        cur = self.root
        for token in path.split('/'):
            if cur and token:
                cur = cur.get(token)

        return sorted(cur.children.keys()) if cur else []

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        cur = self.root
        for token in path.split('/'):
            if token:
                cur = cur.setdefault(token)

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        self.mkdir(filePath)
        self.fileInfo.get(filePath, []).append(content)

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.fileInfo.get(filePath, [])

# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
param_1 = obj.ls("/")
obj.mkdir("/a/b/c")
obj.addContentToFile("/a/b/c/d", "hello")
param_4 = obj.readContentFromFile("/a/b/c/d")
print(param_4)