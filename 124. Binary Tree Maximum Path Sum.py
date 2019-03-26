# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -float('inf')
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0

        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)

        temp = node.val + left + right

        self.res = max(self.res, temp)

        return node.val + max(left, right)


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
    # t2.left = t4
    # t2.right = t5
    print(Solution().maxPathSum(t1))
