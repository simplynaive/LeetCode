# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # # without helper function using stack
        # stack = [(p, q)]
        # node1, node2 = stack.pop()
        # while stack:
        #     if not node1 and not node2:
        #         continue
        #     elif None in [node1, node2]:
        #         return False
        #     else:
        #         if node1.val != node2.val:
        #             return False
        #         stack.append((node1.right, node2.right))
        #         stack.append((node1.left, node2.left))
        # return True

        # with helper function
        if not p and not q:
            return True
        elif p and q:
            if not p.left and not p.right and not q.left and not q.right:
                return p.val == q.val
            print(1)
            return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
        else:
            return False

    def dfs(self, node1, node2):
        if not node1 and node2:
            return False
        elif not node2 and node1:
            return False
        if node1 and node2:
            if node1.val != node2.val:
                return False
            if node1.left and node2.left:
                self.dfs(node1.left, node2.left)
            elif node1.right and node2.right:
                self.dfs(node1.right, node2.right)
            return True


if __name__ == "__main__":
    # build binary tree
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    # t3 = TreeNode(3)
    # t4 = TreeNode(4)
    # t5 = TreeNode(5)
    t1.right = t2
    # t1.right = t3
    # t2.left = t4
    # t2.right = t5

    s1 = TreeNode(1)
    s2 = TreeNode(2)
    # s3 = TreeNode(3)
    # s4 = TreeNode(4)
    # s5 = TreeNode(5)
    s1.right = s2
    # s1.right = s3
    # s2.left = s4
    # s2.right = s5
    print(Solution().isSameTree(t1, s1))
