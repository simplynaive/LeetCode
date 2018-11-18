# Definition for a Node.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(node) for node in root.children) + 1


if __name__ == "__main__":
    # build binary tree
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Preorder: 1, 2, 4, 5, 3
    # Inorder: 4, 2, 5, 1, 3
    # Postorder: 4, 5, 2, 3, 1
    t1 = Node(val=1)
    t2 = Node(2)
    t3 = Node(3)
    t4 = Node(4)
    t5 = Node(5)
    t1.children = t2
    t1.children = t3
    t2.children = t4
    t2.children = t5
    print(Solution().maxDepth(t1))
