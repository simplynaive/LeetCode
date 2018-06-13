

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root is p or root is q:
            return root
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            if root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root


if __name__ == "__main__":
    # build binary tree
    #       6
    #     /   \
    #   2       8
    #  / \     / \
    # 0   4   7   9
    #    / \
    #   3   5
    t0 = TreeNode(0)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t9 = TreeNode(9)
    t6.left = t2
    t6.right = t8
    t2.left = t0
    t2.right = t4
    t8.left = t7
    t8.right = t9
    t4.left = t3
    t4.right = t5
    # traverse
    print(Solution().lowestCommonAncestor(t6, t2, t8))
