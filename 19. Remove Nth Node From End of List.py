# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i, j = 1, 1
        fake = ListNode(0)
        fake.next = head
        node = fake
        while node.next:
            j += 1
            node = node.next
        node = fake
        while node:
            if i == j - n:
                node.next = node.next.next if node.next else None
                return fake.next
            i += 1
            node = node.next


if __name__ == "__main__":
    t0 = ListNode(1)
    t1 = ListNode(2)
    t2 = ListNode(3)
    t3 = ListNode(4)
    t4 = ListNode(5)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t4
    head = Solution().removeNthFromEnd(t0, 2)
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    print(nums)