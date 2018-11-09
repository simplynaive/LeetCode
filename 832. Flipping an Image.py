class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for line in A:
            start, end = 0, len(line) - 1
            while start < end:
                if line[start] != line[end]:
                    m, n = line[start], line[end]
                    line[start] = int(n == 0)
                    line[end] = int(m == 0)
                else:
                    line[start] = int(line[start] == 0)
                    line[end] = int(line[end] == 0)
                start += 1
                end -= 1
            if len(line) % 2 != 0:
                line[int((len(line) - 1) / 2)] = int(line[int((len(line) - 1) / 2)] == 0)
        return A


if __name__ == "__main__":
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(Solution().flipAndInvertImage(A))
