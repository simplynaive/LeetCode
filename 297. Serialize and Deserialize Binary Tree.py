# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root, res):
            if root:
                res.append(str(root.val) + ',')
                dfs(root.left, res)
                dfs(root.right, res)
            else:
                res.append('None,')

        dfs(root, res)
        return ''.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')[:-1]

        def buildTree(data):
            if not data:
                return None
            node = data.pop(0)
            if node == 'None':
                return None
            node = TreeNode(int(node))
            node.left = buildTree(data)
            node.right = buildTree(data)
            return node

        return buildTree(data)





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
    codec = Codec().serialize(t1)
    print(codec)
    print(Codec().deserialize(codec))
