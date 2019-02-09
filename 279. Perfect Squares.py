class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        squares = []
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1
        queue = [(n, 0)]
        while queue:
            for num, dist in queue:
                for square in squares:
                    if num == square:
                        return dist + 1
                    if num < square:
                        break
                    queue.append((num - square, dist + 1))
        return 0


if __name__ == "__main__":
    n = 12
    print(Solution().numSquares(n))
