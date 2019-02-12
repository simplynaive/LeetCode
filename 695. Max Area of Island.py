class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(self.dfs(i, j, grid), res)

        return res

    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return 0

        grid[i][j] = 0

        d = self.dfs(i + 1, j, grid)
        u = self.dfs(i - 1, j, grid)
        r = self.dfs(i, j + 1, grid)
        l = self.dfs(i, j - 1, grid)
        return d + u + r + l + 1


if __name__ == "__main__":
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1]]
    print(Solution().maxAreaOfIsland(grid))
