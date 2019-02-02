# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = 0, 0
        while l1:
            s1 = s1 * 10 + l1.val
            l1 = l1.next
        while l2:
            s2 = s2 * 10 + l2.val
            l2 = l2.next
        s = s1 + s2

        if s == 0:
            return 0
        dummy = ListNode(0)
        curr = dummy
        s = str(s)
        for i in range(len(s)):
            next_node = ListNode(int(s[i]))
            curr.next = next_node
            curr = curr.next
        return dummy.next


if __name__ == "__main__":
    # Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 8 -> 0 -> 7
    l1 = ListNode(7)
    l10 = ListNode(2)
    l11 = ListNode(4)
    l12 = ListNode(3)
    l2 = ListNode(5)
    l20 = ListNode(6)
    l21 = ListNode(4)
    l1.next = l10
    l10.next = l11
    l11.next = l12
    l2.next = l20
    l20.next = l21
    print(Solution().addTwoNumbers(l1, l2))
