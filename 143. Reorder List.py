# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find middle
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        # reverse the latter half
        curr = middle
        last = None

        while curr:
            nextNode = curr.next
            curr.next = last
            last = curr
            curr = nextNode

        # merge
        a, b = head, last
        while b:
            temp = a.next
            a.next = b
            a = temp

            temp = b.next
            b.next = a
            b = temp

        return None


if __name__ == "__main__":
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(4)
    t5 = ListNode(5)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    Solution().reorderList(t1)

    list = []
    node = t1
    while node.next:
        list.append(node.val)
        node = node.next
    list.append(node.val)
    print(list)
