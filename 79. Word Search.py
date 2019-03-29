class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(board, word, i, j):
            if not word:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False

            temp = board[i][j]
            board[i][j] = '0'
            res = dfs(board, word[1:], i - 1, j) or dfs(board, word[1:], i + 1, j) or \
                  dfs(board, word[1:], i, j - 1) or dfs(board, word[1:], i, j + 1)
            board[i][j] = temp
            return res

        if board and word:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if dfs(board, word, i, j):
                        return True
        return False


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = 'ABCCED'
    print(Solution().exist(board, word))
