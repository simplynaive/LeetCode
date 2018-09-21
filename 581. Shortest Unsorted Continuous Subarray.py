class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = sorted(nums)
        start, end = -1, 0
        for i in range(len(nums)):
            if nums[i] != l[i]:
                if start < 0:
                    start = i
                end = i
        if start < 0:
            return 0
        elif end == 0:
            return len(nums) - start
        return end - start + 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().findUnsortedSubarray(nums))
