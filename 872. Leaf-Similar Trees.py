# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        res = []
        self.dfs(root, res)

        fake = TreeNode(0)
        cur_node = fake
        for v in res:
            cur_node.right = TreeNode(v)
            cur_node = cur_node.right
        return fake.right

    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root.val)
            self.dfs(root.right, res)