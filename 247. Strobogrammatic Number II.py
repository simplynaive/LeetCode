class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        one = ['0', '1', '8']
        two = ['00', '11', '88', '69', '96']
        if n == 1:
            return one
        if n == 2:
            return two[1:]
        if n % 2 == 1:
            pre = self.findStrobogrammatic(n - 1)
            mid = one
        else:
            pre = self.findStrobogrammatic(n - 2)
            mid = two
        midIndex = (n - 1) // 2
        return [p[:midIndex] + c + p[midIndex:] for c in mid for p in pre]


if __name__ == "__main__":
    n = 4
    print(Solution().findStrobogrammatic(n))
