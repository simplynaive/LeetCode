class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.map = [None] * self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            return
        index = self.hash(key)
        cur = self.map[index]
        if not cur:
            self.map[index] = ListNode(key)
            return
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.hash(key)
        cur = pre = self.map[index]
        if not cur:
            return
        if cur.val == key:
            self.map[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.val == key:
                    pre.next = cur.next
                    return
                pre = cur
                cur = cur.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.hash(key)
        cur = self.map[index]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

    def hash(self, key):
        return key % self.size

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(2)
obj.remove(2)
print(obj.contains(2))