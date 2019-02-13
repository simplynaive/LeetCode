# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res, 0)
        return res

    def dfs(self, node, res, depth):
        if not node:
            return

        if len(res) == depth:
            res.append(node.val)

        self.dfs(node.right, res, depth + 1)
        self.dfs(node.left, res, depth + 1)


if __name__ == "__main__":
    # build binary tree
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6
    print(Solution().rightSideView(t1))
