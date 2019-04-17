
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # stack = []
        # pre = None
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     if pre and root.val <= pre.val:
        #         return False
        #     pre = root
        #     root = root.right
        # return True


        if not root:
            return True

        def dfs(node, lower, upper):
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False

            if node.left:
                left = dfs(node.left, lower, node.val)
            else:
                left = True

            if left:
                if node.right:
                    right = dfs(node.right, node.val, upper)
                else:
                    right = True
                return right
            else:
                return False

        return dfs(root, None, None)


if __name__ == "__main__":
    # # build binary tree
    # #     1
    # #    / \
    # #   2   3
    # #  / \
    # # 4   5
    # t1 = TreeNode(1)
    # t2 = TreeNode(2)
    # t3 = TreeNode(3)
    # t4 = TreeNode(4)
    # t5 = TreeNode(5)
    # t1.left = t2
    # t1.right = t3
    # t2.left = t4
    # t2.right = t5

    t0 = TreeNode(0)
    t1 = TreeNode(-1)
    t0.right = t1
    print(Solution().isValidBST(t0))
