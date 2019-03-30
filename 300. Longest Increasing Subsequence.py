class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #             print(i, j, dp)
        # return max(dp)

        temp = []
        for num in nums:

            left = 0
            right = len(temp)
            while left < right:
                mid = left + (right - left) // 2
                if temp[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left >= len(temp):
                temp.append(num)
            else:
                temp[left] = num
        return len(temp)


if __name__ == "__main__":
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(Solution().lengthOfLIS(nums))
