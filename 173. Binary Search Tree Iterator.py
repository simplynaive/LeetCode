# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        res = []
        for s in self.stack:
            res.append(s.val)
        print(res)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        right = node.right
        while right:
            self.stack.append(right)
            right = right.left
        return node.val


if __name__ == "__main__":
    # build binary tree
    #     7
    #    / \
    #   5   9
    #  / \
    # 4   6
    # Inorder: 4, 5, 6, 7, 9
    t1 = TreeNode(7)
    t2 = TreeNode(5)
    t3 = TreeNode(9)
    t4 = TreeNode(4)
    t5 = TreeNode(6)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    # traverse
    i, v = BSTIterator(t1), []
    while i.hasNext():
        v.append(i.next())
    print(v)
