class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preMax = 0
        currMax = 0
        for i in range(len(nums)):
            t = currMax
            currMax = max(preMax + nums[i], currMax)
            preMax = t
        return currMax


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
