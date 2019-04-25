class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ranked = sorted(nums, reverse=True)
        dic = {}
        dic[ranked[0]] = "Gold Medal"
        if len(nums) > 1:
            dic[ranked[1]] = 'Silver Medal'
        if len(nums) > 2:
            dic[ranked[2]] = 'Bronze Medal'
        for i in range(3, len(nums)):
            dic[ranked[i]] = str(i + 1)
        res = []
        for n in nums:
            res.append(dic[n])
        return res


if __name__ == "__main__":
    nums = [5, 3, 2, 4, 1]
    print(Solution().findRelativeRanks(nums))
