class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []

        flag = False

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                i -= 1
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        flag = True
                        nums[i + 1:] = sorted(nums[i + 1:])
                        break
            if flag:
                break
        if not flag:
            nums.sort()

        print(nums)


if __name__ == "__main__":
    nums = [3, 2, 1]
    print(Solution().nextPermutation(nums))
