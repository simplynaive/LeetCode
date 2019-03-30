class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        l, r = 0, 1
        res = 0
        while r < len(nums):
            if nums[r] <= nums[r - 1]:
                l = r
            r += 1
            res = max(res, r - l)
        return res


if __name__ == "__main__":
    nums = [1, 3, 5, 4, 7]
    print(Solution().findLengthOfLCIS(nums))
