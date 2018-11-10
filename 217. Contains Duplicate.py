class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution().containsDuplicate(nums))
