class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums or k > len(nums):
            return 0
        sums = [nums[0]]
        for i in range(len(nums)):
            sums.append(sums[-1]+nums[i])
        max_sum = sum(nums[:k])
        for j in range(len(sums)-k):
            max_sum = max(max_sum, sums[j+k]-sums[j])
        return max_sum / float(k)


if __name__ == "__main__":
    nums = [0, 1, 1, 3, 3]
    k = 4
    print(Solution().findMaxAverage(nums, k))
