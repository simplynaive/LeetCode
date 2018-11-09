class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 0
        for i in range(len(A)):
            if A[j] % 2 == 1:
                A.append(A[j])
                A.pop(j)
                j -= 1
            j += 1
        return A


if __name__ == "__main__":
    A = [3, 1, 2, 4]
    print(Solution().sortArrayByParity(A))
