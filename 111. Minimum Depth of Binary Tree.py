

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0
        # if not root.right or not root.left:
        #     return self.minDepth(root.left) + self.minDepth(root.right) + 1
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        if not root:
            return 0
        children = [root.left, root.right]
        if not any(children):
            return 1

        min_depth = float('inf')
        for child in children:
            if child:
                min_depth = min(self.minDepth(child), min_depth)
        return min_depth + 1


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
    print(Solution().minDepth(t1))
