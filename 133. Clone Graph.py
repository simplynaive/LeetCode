# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        rootCopy = UndirectedGraphNode(node.label)
        stack = [node]
        visited = dict()
        visited[node.label] = rootCopy
        while stack:
            top = stack.pop()

            for n in top.neighbors:
                if n.label not in visited:
                    stack.append(n)
                    visited[n.label] = UndirectedGraphNode(n.label)
                visited[top.label].neighbors.append(visited[n.label])

        return rootCopy


if __name__ == "__main__":
    n1 = UndirectedGraphNode(1)
    n2 = UndirectedGraphNode(2)
    n3 = UndirectedGraphNode(3)
    n4 = UndirectedGraphNode(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n3.neighbors = [n1, n3]
    print(Solution().cloneGraph(n1).label)
