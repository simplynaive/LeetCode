class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        n = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[n] = nums[i]
                n += 1
        return n


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    print(nums[:Solution().removeElement(nums, val)])
