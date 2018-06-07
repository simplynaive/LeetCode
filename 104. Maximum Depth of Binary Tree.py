

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # # divided conquer
    # def maxDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #     maxleft = self.maxDepth(root.left)
    #     maxright = self.maxDepth(root.right)
    #     return max(maxleft, maxright) + 1

    # traverse
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        if not root:
            return 0
        self.helper(root, 1)
        return self.depth

    def helper(self, root, curDepth):
        if not root:
            return
        self.depth = max(self.depth, curDepth)

        self.helper(root.left, curDepth + 1)
        self.helper(root.right, curDepth + 1)


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
    # traverse
    print(Solution().maxDepth(t1))
