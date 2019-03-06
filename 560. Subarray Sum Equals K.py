from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sums = [nums[0]]
        # for i in range(1, len(nums)):
        #     sums.append(sums[i - 1] + nums[i])
        # diff = dict()
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         d = sums[j] - sums[i] + nums[i]
        #         if d in diff:
        #             diff[d] += 1
        #         else:
        #             diff[d] = 1
        # if k in diff:
        #     return diff[k]
        # else:
        #     return 0
        dic = {0: 1}
        res = pre_sum = 0
        for num in nums:
            pre_sum += num
            res += dic.get(pre_sum - k, 0)
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
        return res


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))
