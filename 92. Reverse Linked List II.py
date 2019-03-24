# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        cnt = 1
        curr = head
        pre = None
        front = rear = tail = reverseHead = None
        while curr:
            t = curr.next
            if cnt == m - 1:
                front = curr
            if cnt == m:
                tail = curr
            if cnt == n + 1:
                rear = curr
            if cnt == n:
                reverseHead = curr
            if m <= cnt <= n:
                curr.next = pre
            pre = curr
            curr = t
            cnt += 1
        if front:
            front.next = reverseHead
        if tail:
            tail.next = rear
        if m == 1:
            return reverseHead
        return head



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
    m, n = 2, 4
    node = Solution().reverseBetween(t0, m, n)
    stack = []
    while node:
        stack.append(node.val)
        node = node.next
    print(stack)