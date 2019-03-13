class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start, end = 0, len(A) - 1
        while start < end:
            mid = (start + end) // 2
            if A[mid] < A[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return end


if __name__ == "__main__":
    nums = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    print(Solution().peakIndexInMountainArray(nums))
