class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsum = res = nums[0]
        for num in nums[1:]:
            res = max(num, num + res)
            maxsum = max(maxsum, res)
        return maxsum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
