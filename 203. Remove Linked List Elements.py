# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head or not val:
            return None
        node = head
        while node.next and node.next.next:
            if node.next.val == val:
                node.next.val = node.next.next.val
                node.next = node.next.next
            else:
                node = node.next
        if node.next:
            if node.next.val == val:
                node.next = None
        if head.val == val:
            return head.next
        return head


if __name__ == "__main__":
    nums = [1, 2, 6, 3, 4, 5, 6]
    t0 = ListNode(1)
    t1 = ListNode(2)
    t2 = ListNode(6)
    t3 = ListNode(3)
    t4 = ListNode(4)
    t5 = ListNode(5)
    t6 = ListNode(6)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6
    print(Solution().removeElements(t0, 6))

    list = []
    node = t0
    while node.next:
        list.append(node.val)
        node = node.next
    list.append(node.val)
    print(list)
