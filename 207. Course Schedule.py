class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = [-1] * (numCourses + 1)

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
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(Solution().canFinish(numCourses, prerequisites))
