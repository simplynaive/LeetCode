class Solution:
    def numMagicSquaresInside(self, grid: 'List[List[int]]') -> 'int':
        count = 0

        def helper(a, b, c, d, e, f, g, h, i):
            return sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10)) and \
                   a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if helper(grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i + 1][j], grid[i + 1][j + 1],
                          grid[i + 1][j + 2], grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]):
                    count += 1
        return count


if __name__ == "__main__":
    board = [[4, 3, 8, 4],
             [9, 5, 1, 9],
             [2, 7, 6, 2]]
    # board = [[4, 7, 8],
    #          [9, 5, 1],
    #          [2, 3, 6]]
    print(Solution().numMagicSquaresInside(board))
