class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = []
        if v1:
            self.queue.append(v1)
        if v2:
            self.queue.append(v2)

    def next(self):
        """
        :rtype: int
        """
        v = self.queue.pop(0)
        res = v.pop(0)
        if v:
            self.queue.append(v)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue != []


# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1, 2]
v2 = [3, 4, 5, 6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext():
    v.append(i.next())
print(v)
