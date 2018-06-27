class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp = -float("inf")
        j = 0
        for i in range(len(nums)):
            if nums[i] > temp:
                temp = nums[i]
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))
