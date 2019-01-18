

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # if not root:
        #     return
        # self.flatten(root.left)
        # self.flatten(root.right)
        # node = root
        # if not node.left:
        #     return
        # node = node.left
        # while node.right:
        #     node = node.right
        # node.right = root.right
        # root.right = root.left
        # root.left = None
        # return

        if not root:
            return
        res = []
        self.dfs(root, res)
        for i in range(len(res) - 1):
            res[i].right = res[i + 1]
            res[i].left = None
        res[-1].left = None

    def dfs(self, node, res):
        if node:
            res.append(node)
            self.dfs(node.left, res)
            self.dfs(node.right, res)


if __name__ == "__main__":
    # build binary tree
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t1.left = t2
    t1.right = t5
    t2.left = t3
    t2.right = t4
    t5.right = t6
    # traverse
    print(Solution().flatten(t1))
