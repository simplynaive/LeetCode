class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if 0 < len(A) <= 2:
            return True
        if self.trend(A) == 'equal':
            return True
        elif self.trend(A) == 'ascend':
            for i in range(1, len(A)):
                if A[i - 1] > A[i]:
                    return False
        elif self.trend(A) == 'descend':
            for i in range(1, len(A)):
                if A[i - 1] < A[i]:
                    return False

        return True

    def trend(self, A):
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                return 'descend'
            elif A[i - 1] < A[i]:
                    return 'ascend'
        return 'equal'


if __name__ == "__main__":
    A = [6, 5, 4, 4]
    print(Solution().isMonotonic(A))