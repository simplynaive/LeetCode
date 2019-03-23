# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headB
            if pB:
                pB = pB.next
            else:
                pB = headA
        return pA


if __name__ == "__main__":
    # Input: 1->2->4, 1->3->4
    l10 = ListNode(0)
    l11 = ListNode(9)
    l12 = ListNode(1)
    l13 = ListNode(2)
    l14 = ListNode(4)
    l10.next = l11
    l11.next = l12
    l12.next = l13
    l13.next = l14

    l20 = ListNode(3)
    l21 = ListNode(2)
    l22 = ListNode(4)
    l20.next = l21
    l21.next = l22

    print(Solution().getIntersectionNode(l10, l20).val)
