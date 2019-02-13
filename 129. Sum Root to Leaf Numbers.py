# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, 0)

    def dfs(self, node, value):
        if not node:
            return 0
        cur_value = value * 10 + node.val
        print(node.val, cur_value)
        s = self.dfs(node.left, cur_value) + self.dfs(node.right, cur_value)
        if s == 0:
            return cur_value
        else:
            return s


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
    print(Solution().sumNumbers(t1))
