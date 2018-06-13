

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
        self.curt = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curt is not None or len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        while self.curt is not None:
            self.stack.append(self.curt)
            self.curt = self.curt.left
        self.curt = self.stack.pop()
        nxt = self.curt
        self.curt = self.curt.right
        return nxt.val


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
    i, v = BSTIterator(t1), []
    while i.hasNext():
        v.append(i.next())
    print(v)
