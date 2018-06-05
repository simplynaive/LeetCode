import time

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n
        if n == 1:
            return 1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        if isBadVersion(end):
            return end
        return -1


def isBadVersion(m):
    if m >= 2:
        return True
    return False


if __name__ == "__main__":
    n = 2
    start = time.time()
    solution = Solution()
    print(solution.firstBadVersion(n))
    end = time.time()
    print("runtime = ", end - start)
