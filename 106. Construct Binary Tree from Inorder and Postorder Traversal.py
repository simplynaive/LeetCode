# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_index = inorder.index(postorder.pop(-1))
            root = TreeNode(inorder[root_index])
            root.right = self.buildTree(inorder[root_index + 1:], postorder)
            root.left = self.buildTree(inorder[: root_index], postorder)
            return root


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    print(Solution().buildTree(inorder, postorder))
