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
    print(Solution().sortedListToBST(t0))
