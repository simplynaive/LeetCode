import time


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        target = nums[-1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if nums[mid] <= target:
                end = mid
            else:
                start = mid

        return min(nums[start], nums[end])


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]

    start = time.time()
    solution = Solution()
    print(solution.findMin(nums))
    end = time.time()
    print("runtime = ", end - start)
