# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        dic = dict()

        stack = [[root, 0]]
        while stack:
            root, level = stack.pop(0)
            if root:
                if level not in dic:
                    dic[level] = [root.val]
                else:
                    dic[level].append(root.val)
                if root.left:
                    stack.append([root.left, level - 1])
                if root.right:
                    stack.append([root.right, level + 1])

        for i in range(min(dic.keys()), max(dic.keys()) + 1):
            res.append(dic[i])

        return res


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
    print(Solution().verticalOrder(t1))