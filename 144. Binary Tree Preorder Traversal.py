

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # iterative
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

    # # recursive
    # def preorderTraversal(self, root):
    #     res = []
    #     self.dfs(root, res)
    #     return res
    #
    # def dfs(self, root, res):
    #     if root:
    #         res.append(root.val)
    #         self.dfs(root.left, res)
    #         self.dfs(root.right, res)


if __name__ == "__main__":
    # build binary tree
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Preorder: 1, 2, 4, 5, 3
    # Inorder: 4, 2, 5, 1, 3
    # Postorder: 4, 5, 2, 3, 1
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
    print(Solution().preorderTraversal(t1))
