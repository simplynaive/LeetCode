import time


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if not A and not B:
            return True
        for i in range(len(A)):
            if A == B[len(A) - i:] + B[:len(A) - i]:
                return True
        return False


if __name__ == "__main__":
    A = 'abcde'
    B = 'cdeab'
    start = time.time()
    solution = Solution()
    print(solution.rotateString(A, B))
    end = time.time()
    print("runtime = ", end - start)
