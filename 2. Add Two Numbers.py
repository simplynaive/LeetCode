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
        dummyhead = ListNode(0)
        curr = dummyhead
        p, q = l1, l2
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            curr_sum = carry + x + y
            carry = curr_sum // 10
            curr.next = ListNode(curr_sum % 10)
            curr = curr.next
            p = p.next if p else p
            q = q.next if q else q
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyhead.next


if __name__ == "__main__":
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807.
    l1 = ListNode(2)
    l10 = ListNode(4)
    l11 = ListNode(3)
    l2 = ListNode(5)
    l20 = ListNode(6)
    l21 = ListNode(4)
    l1.next = l10
    l10.next = l11
    l2.next = l20
    l20.next = l21
    print(Solution().addTwoNumbers(l1, l2))
