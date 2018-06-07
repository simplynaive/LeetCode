

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.isMatch(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, s, t):
        if not (s and t):
            return s is t
        left = self.isMatch(s.left, t.left)
        right = self.isMatch(s.right, t.right)
        if s.val == t.val and left and right:
            return True
        else:
            return False


if __name__ == "__main__":
    # build binary tree s
    #     3
    #    / \
    #   4   5
    #  / \
    # 1   2
    s1 = TreeNode(1)
    s2 = TreeNode(2)
    s3 = TreeNode(3)
    s4 = TreeNode(4)
    s5 = TreeNode(5)
    s3.left = s4
    s3.right = s5
    s4.left = s1
    s4.right = s2

    # s0 = TreeNode(0)
    # s2.left = s0

    # build binary tree t
    #   4
    #  / \
    # 1   2
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t4 = TreeNode(4)
    t4.left = t1
    t4.right = t2
    # traverse
    print(Solution().isSubtree(s3, t4))
