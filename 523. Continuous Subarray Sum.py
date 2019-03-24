class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        if sum(nums) == 0 and len(nums) >= 2:
            return True
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        dic = {0: -1}
        s = 0
        for i in range(len(nums)):
            s = (s + nums[i]) % k
            if s in dic and i - dic[s] > 1:
                return True
            if s not in dic:
                dic[s] = i
        return False


if __name__ == "__main__":
    nums = [1, 1]
    k = -1
    print(Solution().checkSubarraySum(nums, k))
