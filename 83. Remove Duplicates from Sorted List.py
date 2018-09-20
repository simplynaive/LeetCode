# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        node = head
        while node:
            while node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return

if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3]
    t0 = ListNode(1)
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(3)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t4
    Solution().deleteDuplicates(t0)
    node = t0
    list = []
    while node.next:
        print(node.val + ' -> ')
        list.append(node.val)
        node = node.next
    print(node.val)
