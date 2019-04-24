class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = dict()
        # for n in nums:
        #     if n in d.keys():
        #         d[n] += 1
        #     else:
        #         d[n] = 1
        # return list({k: v for k, v in d.items() if v == 1}.keys())[0]

        # bit manipulation
        a = 0
        for i in nums:
            a ^= i
        return a

    #     def singleNumber(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #         if len(nums) == 1:
    #             return nums[0]
    #         nums = sorted(nums)
    #         for i in range(len(nums)):
    #             if i == 0 and nums[i] != nums[i + 1]:
    #                 return nums[i]
    #             elif i == len(nums) - 1:
    #                 if nums[i] != nums[i - 1]:
    #                     return nums[i]
    #             elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
    #                 return nums[i]
    #         return 0


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))
