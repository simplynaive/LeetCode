# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return

if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    t0 = ListNode(-10)
    t1 = ListNode(-3)
    t2 = ListNode(0)
    t3 = ListNode(5)
    t4 = ListNode(9)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t4
    Solution().deleteNode(t3)
    node = t0
    list = []
    while node.next:
        list.append(node.val)
        node = node.next
    list.append(node.val)
    print(list)
