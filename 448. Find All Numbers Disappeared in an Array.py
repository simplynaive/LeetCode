class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Could you do it without extra space and in O(n) runtime?
        if not nums:
            return nums
        res = []
        n = len(nums)
        nums = sorted(set(nums))
        if nums[0] != 1:
            nums.append(1)
            res.append(1)
            nums = sorted(nums)
        if nums[-1] < n:
            nums.append(n)
            res.append(n)
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                for j in range(1, nums[i + 1] - nums[i]):
                    res.append(nums[i] + j)
        return sorted(res)


if __name__ == "__main__":
    nums = [2, 2]
    print(Solution().findDisappearedNumbers(nums))
