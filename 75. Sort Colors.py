class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            for i in range(len(nums)):
                for j in range(i, len(nums)):
                    if nums[i] > nums[j]:
                        t = nums[i]
                        nums[i] = nums[j]
                        nums[j] = t
        return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution().sortColors(nums))
