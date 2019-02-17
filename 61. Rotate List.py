# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        i, j = 0, 0
        node = head
        while node.next:
            j += 1
            node = node.next
        j += 1
        k = k % j
        if k == 0:
            return head
        node.next = head
        node = head
        while node:
            if i == j - k - 1:
                print(i, node.val)
                res = node.next
                node.next = None
                return res
            i += 1
            node = node.next


if __name__ == "__main__":
    t0 = ListNode(1)
    # t1 = ListNode(2)
    # t2 = ListNode(3)
    # t3 = ListNode(4)
    # t4 = ListNode(5)
    # t0.next = t1
    # t1.next = t2
    # t2.next = t3
    # t3.next = t4
    head = Solution().rotateRight(ListNode(None), 0)
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    print(nums)