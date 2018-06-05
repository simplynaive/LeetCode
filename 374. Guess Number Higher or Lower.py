import time


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n
        mid = int(n / 2)
        if n == 1:
            return n
        while start + 1 < end:
            mid = int((start + end) / 2)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                start = mid
            elif guess(mid) == -1:
                end = mid

        if guess(start) == 0:
            return start
        if guess(end) == 0:
            return end


def guess(m):
    pick = 2
    if m < pick:
        return 1
    elif m > pick:
        return -1
    elif m == pick:
        return 0
    return -2


if __name__ == "__main__":
    n = 2
    start = time.time()
    solution = Solution()
    print(solution.guessNumber(n))
    end = time.time()
    print("runtime = ", end - start)
