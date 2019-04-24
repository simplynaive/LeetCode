# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res[:: -1]

    def dfs(self, node, level, res):
        if node:
            if len(res) < level + 1:
                res.append([])
            res[level].append(node.val)
            self.dfs(node.left, level + 1, res)
            self.dfs(node.right, level + 1, res)


if __name__ == "__main__":
    # build binary tree
    #     3
    #    / \
    #   9  20
    #  / \
    # 15  7
    t3 = TreeNode(3)
    t9 = TreeNode(9)
    t20 = TreeNode(20)
    t15 = TreeNode(15)
    t7 = TreeNode(7)
    t3.left = t9
    t3.right = t20
    t9.left = t15
    t9.right = t7
    print(Solution().levelOrderBottom(t3))
