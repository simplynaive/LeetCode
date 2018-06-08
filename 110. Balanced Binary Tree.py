

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root) != -1

    def helper(self, root):
        if not root:
            return True
        leftdepth = self.helper(root.left)
        rightdepth = self.helper(root.right)
        if leftdepth == -1 or rightdepth == -1 or abs(leftdepth - rightdepth) > 1:
            return -1
        return 1 + max(leftdepth, rightdepth)

if __name__ == "__main__":
    # build binary tree
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    # # build binary tree
    # #        1
    # #       / \
    # #      2   3
    # #     / \
    # #    4   5
    # #   / \
    # #  6   7
    # t1 = TreeNode(1)
    # t2 = TreeNode(2)
    # t3 = TreeNode(3)
    # t4 = TreeNode(4)
    # t5 = TreeNode(5)
    # t6 = TreeNode(6)
    # t7 = TreeNode(7)
    # t1.left = t2
    # t1.right = t3
    # t2.left = t4
    # t2.right = t5
    # t4.left = t6
    # t4.right = t7

    # traverse
    print(Solution().isBalanced(t1))
