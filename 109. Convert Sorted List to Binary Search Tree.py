# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next

        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root


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
