import time

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)
        for n in nums:
            if n >= target:
                return nums.index(n)
        return 0


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 7
    start = time.time()
    solution = Solution()
    print(solution.searchInsert(nums, target))
    end = time.time()
    print("runtime = ", end - start)
