class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    elif s > target:
                        r -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0, 0]
    target = -1
    print(Solution().fourSum(nums, target))
