class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        B = sorted(B)
        diff = (sum(A) - sum(B)) // 2
        for a in A:
            if len(B) < 3:
                if a - diff in B:
                    return [a, a - diff]
            else:
                if B[0] == a - diff or B[-1] == a - diff:
                    return [a, a - diff]
                start, end = 0, len(B) - 1
                mid = (start + end) // 2
                while end - start > 1:
                    if a - diff == B[mid]:
                        return [a, a - diff]
                    if a - diff > B[mid]:
                        start = mid
                        mid = (start + end) // 2
                    elif a - diff < B[mid]:
                        end = mid
                        mid = (start + end) // 2
        return [0, 0]


if __name__ == "__main__":
    A = [32, 39, 8, 41, 9, 2, 24, 33, 32, 25, 10, 29, 24, 1, 14, 20, 37, 49, 49, 29]
    B = [36, 86, 80, 97, 26, 100, 60, 65, 24, 93]
    print(Solution().fairCandySwap(A, B))
