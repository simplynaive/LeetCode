# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        flag = False
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if flag:
            visited = []
            node = head
            while node not in visited:
                visited.append(node)
                node = node.next
                if node.next in visited:
                    return node.next
        return None


if __name__ == "__main__":
    t0 = ListNode(3)
    t1 = ListNode(2)
    t2 = ListNode(0)
    t3 = ListNode(4)
    t0.next = t1
    t1.next = t2
    t2.next = t3
    t3.next = t1
    print(Solution().detectCycle(t0))
