# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head:
    #         return
    #     values = [head.val]
    #     while head.next:
    #         values.append(head.next.val)
    #         head = head.next
    #     a = []
    #     a.append(ListNode(values[0]))
    #     for i in range(1, len(values)):
    #         a.append(ListNode(values[i]))
    #         a[i].next = a[i - 1]
    #     return a[-1]

    # inplace
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        pre = None
        curr = head
        while curr:
            t = curr.next
            curr.next = pre
            pre = curr
            curr = t
        return pre


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
    print(Solution().reverseList(t0))