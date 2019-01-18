# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        res = []
        self.dfs(root, 0, res)
        for i in range(len(res)):
            for k in range(len(res[i]) - 1):
                res[i][k].next = res[i][k + 1]

    def dfs(self, node, level, res):
        if node:
            if len(res) < level + 1:
                res.append([])
            res[level].append(node)
            self.dfs(node.left, level + 1, res)
            self.dfs(node.right, level + 1, res)


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
    print(Solution().connect(t1))
