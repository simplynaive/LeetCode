import time


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return nums.index(max(nums[start], nums[end]))


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]
    start = time.time()
    solution = Solution()
    print(solution.findPeakElement(nums))
    end = time.time()
    print("runtime = ", end - start)
