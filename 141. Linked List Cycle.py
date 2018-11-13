# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    t0 = ListNode(1)
    t1 = ListNode(2)
    t2 = ListNode(6)
    t3 = ListNode(1)
    t4 = ListNode(2)
    t5 = ListNode(6)
    t6 = ListNode(1)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6
    print(Solution().hasCycle(t0))
