

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # divided conquer
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.path = []
        if not root:
            return self.path
        self.dfs(root, [])
        return self.path

    def dfs(self, node, step):
        step.append(str(node.val))
        if node.left is None and node.right is None:
            self.path.append('->'.join(step))
            step.pop()
            return

        if node.left:
            self.dfs(node.left, step)

        if node.right:
            self.dfs(node.right, step)

        step.pop()


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
    print(Solution().binaryTreePaths(t1))
