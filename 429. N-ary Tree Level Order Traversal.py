# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur_level = []
            next_level = []
            for node in stack:
                cur_level.append(node.val)
                for child in node.children:
                    next_level.append(child)
            stack = next_level
            res.append(cur_level)
        return res


if __name__ == "__main__":
    # build binary tree
    #       1
    #    /  |  \
    #   3   2   4
    #  / \
    # 5   6
    t6 = Node(6, [])
    t5 = Node(5, [])
    t4 = Node(4, [])
    t2 = Node(2, [])
    t3 = Node(3, [t5, t6])
    t1 = Node(1, [t3, t2, t4])
    print(Solution().levelOrder(t1))
