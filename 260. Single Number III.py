class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        dic = dict()
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        res = []
        for i in dic.keys():
            if dic[i] == 1:
                res.append(i)
        return res


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]
    print(Solution().singleNumber(nums))
