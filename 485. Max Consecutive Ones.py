class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_pos = 0
        last_len = 0
        if sum(nums) == 0:
            return 0
        elif sum(nums) == len(nums):
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                if last_pos == 0:
                    last_len = i
                last_len = max(i - last_pos - 1, last_len)
                last_pos = i
        return max(last_len, len(nums) - last_pos - 1)


if __name__ == "__main__":
    nums = [0, 1]
    print(Solution().findMaxConsecutiveOnes(nums))
