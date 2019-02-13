class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board:
            for j in range(len(board[0])):
                if board[0][j] == 'O':
                    self.mark(0, j, board)
                if board[-1][j] == 'O':
                    self.mark(len(board) - 1, j, board)

            for i in range(len(board)):
                if board[i][0] == 'O':
                    self.mark(i, 0, board)
                if board[i][-1] == 'O':
                    self.mark(i, len(board[0]) - 1, board)

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == -1:
                        board[i][j] = 'O'
                    else:
                        board[i][j] = 'X'

        return board

    def mark(self, i, j, board):
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != 'O':
            return

        board[i][j] = -1

        self.mark(i - 1, j, board)
        self.mark(i + 1, j, board)
        self.mark(i, j - 1, board)
        self.mark(i, j + 1, board)


if __name__ == "__main__":
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    print(Solution().solve(board))
