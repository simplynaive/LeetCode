# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        def reverse(head):
            pre, cur, next = None, head, head
            cnt = 0
            while cnt < k:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
                cnt += 1
            return cur, pre

        cnt = 0
        curr = head
        while curr and cnt < k:
            curr = curr.next
            cnt += 1
        if cnt < k:
            return head
        nextHead, pre = reverse(head)
        head.next = self.reverseKGroup(nextHead, k)
        return pre



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
    k = 2
    node = Solution().reverseKGroup(t0, k)
    stack = []
    while node:
        stack.append(node.val)
        node = node.next
    print(stack)