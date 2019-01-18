# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        paths = []
        self.dfs(root, sum, [], paths)
        return paths

    def dfs(self, node, sum, path, paths):
        if not node.left and not node.right and node.val == sum:
            path.append(node.val)
            paths.append(path)

        sum -= node.val

        if node.left:
            self.dfs(node.left, sum, path + [node.val], paths)
        if node.right:
            self.dfs(node.right, sum, path + [node.val], paths)


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

    sum = 8
    print(Solution().pathSum(t1, sum))
