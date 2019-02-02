# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def sortList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     nums = []
    #     while head:
    #         nums.append(head.val)
    #         head = head.next
    #     nums = sorted(nums)
    #     dummy = ListNode(0)
    #     curr_node = dummy
    #     for num in nums:
    #         next_node = ListNode(num)
    #         curr_node.next = next_node
    #         curr_node = next_node
    #     return dummy.next

    # merge sort, recursively
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    # merge in-place without dummy node
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else:
                pre.next = r
                r = r.next
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head

    def print_list(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums


if __name__ == "__main__":
    t0 = ListNode(-1)
    t1 = ListNode(5)
    t2 = ListNode(3)
    t3 = ListNode(4)
    t4 = ListNode(0)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t4
    head = Solution().sortList(t0)
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    print(nums)
