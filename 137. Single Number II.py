class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        dic = dict()
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for i in dic.keys():
            if dic[i] == 1:
                return i
        return -1


if __name__ == "__main__":
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(Solution().singleNumber(nums))
