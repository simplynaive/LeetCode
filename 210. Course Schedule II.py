class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = [-1] * (numCourses + 1)
        res = []

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 0:
                return True
            visited[course] = 1
            for j in graph[course]:
                if not dfs(j):
                    return False
            visited[course] = 0
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(Solution().findOrder(numCourses, prerequisites))
