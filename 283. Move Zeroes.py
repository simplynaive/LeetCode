class Solution:
    # def moveZeroes(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     j = 0
    #     for i in range(len(nums)):
    #         if nums[j] == 0:
    #             nums.pop(j)
    #             nums.append(0)
    #             j -= 1
    #         j += 1
    #     return nums

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        nums[i:] = [0] * (len(nums) - i)
        return nums


if __name__ == "__main__":
    nums = [0, 0, 1]
    print(Solution().moveZeroes(nums))
