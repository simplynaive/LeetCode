class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.label(grid, i, j)
        return count

    def label(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = -1
        self.label(grid, i+1, j)
        self.label(grid, i-1, j)
        self.label(grid, i, j+1)
        self.label(grid, i, j-1)


if __name__ == "__main__":
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1]]
    print(Solution().numIslands(grid))
