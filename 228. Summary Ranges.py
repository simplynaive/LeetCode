class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        i, j = 0, 0
        res = []
        while j < len(nums) - 1:

            if nums[j] - nums[i] == j - i:
                j += 1
            else:
                if j - i == 1:
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[i]) + '->' + str(nums[j - 1]))
                i = j
                j = i + 1
            if j == len(nums) - 1:
                if nums[j] - nums[j - 1] != 1:
                    res.append(str(nums[j]))
                else:
                    res.append(str(nums[i]) + '->' + str(nums[j]))
        return sorted(res, key=lambda x: int(x.split('->')[0]))


if __name__ == "__main__":
    nums = [-2147483648,-2147483647,2147483647]
    print(Solution().summaryRanges(nums))
