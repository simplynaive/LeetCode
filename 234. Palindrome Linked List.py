# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = None
        while slow:
            nxt = slow.next
            slow.next = tail
            tail = slow
            slow = nxt
        while tail and head:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True


if __name__ == "__main__":
    if __name__ == "__main__":
        nums = [1, 0, 2, 1]
        t0 = ListNode(1)
        t1 = ListNode(2)
        t2 = ListNode(0)
        t3 = ListNode(2)
        t4 = ListNode(1)
        t0.next = t1
        t1.next = t2
        t2.next = t3
        t3.next = t4
        print(Solution().isPalindrome(t0))
