# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            inner = self.helper(left.right, right.left)
            outer = self.helper(left.left, right.right)

            return outer and inner
        return False


if __name__ == "__main__":
    # build binary tree
    #      1
    #     / \
    #    2   2
    #   / \ / \
    #  3  4 4  3
    t1 = TreeNode(1)
    t21 = TreeNode(2)
    t22 = TreeNode(2)
    t31 = TreeNode(3)
    t32 = TreeNode(3)
    t41 = TreeNode(4)
    t42 = TreeNode(4)
    t1.left = t21
    t1.right = t22
    t21.left = t31
    t21.right = t41
    t22.left = t42
    t22.right = t32
    print(Solution().isSymmetric(t1))
