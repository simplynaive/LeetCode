class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum = 0
        for i in range(len(nums)//2):
            sum += nums[2*i]
        return sum


if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    print(Solution().arrayPairSum(nums))
