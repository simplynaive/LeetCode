class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n in dic.keys():
                dic[n] += 1
            else:
                dic[n] = 1
        res = sorted(dic, key=lambda x: dic[x])[-k:]
        res.reverse()
        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
