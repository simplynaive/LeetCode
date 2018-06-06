

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # iterative
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            while root.left:
                stack.append(root)
                root = root.left
            while root.right:
                stack.append(root)
                root = root.right
            node = stack.pop()
            res.append(node.val)
        return res

    # # recursive
    # def postorderTraversal(self, root):
    #     res = []
    #     self.dfs(root, res)
    #     return res
    #
    # def dfs(self, root, res):
    #     if root:
    #         self.dfs(root.left, res)
    #         self.dfs(root.right, res)
    #         res.append(root.val)


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
    print(Solution().postorderTraversal(t1))
