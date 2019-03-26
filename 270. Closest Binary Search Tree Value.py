
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        node = root
        res = root.val
        while node:
            if abs(node.val - target) < abs(res - target):
                res = node.val
            if node.val > target:
                node = node.left
            else:
                node = node.right
        return res


if __name__ == "__main__":
    # build binary tree
    #     4
    #    / \
    #   2   5
    #  / \
    # 1   3
    t1 = TreeNode(4)
    t2 = TreeNode(2)
    t3 = TreeNode(5)
    t4 = TreeNode(1)
    t5 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    target = 3.732421
    print(Solution().closestValue(t1, target))
