# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # cur = ListNode(-float('inf'))

        def mergeTwoLists(l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            root = cur = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return root.next

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists


if __name__ == "__main__":
    # Input: 1->2->4, 1->3->4
    # Output: 1->1->2->3->4->4
    l10 = ListNode(1)
    l11 = ListNode(2)
    l12 = ListNode(4)
    l10.next = l11
    l11.next = l12

    l20 = ListNode(1)
    l21 = ListNode(3)
    l22 = ListNode(4)
    l20.next = l21
    l21.next = l22

    print(Solution().mergeKLists([l10, l20]))