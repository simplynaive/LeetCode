class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dic = {}
        # for n in range(len(nums) + 1):
        #     dic[n] = 1
        #
        # for n in nums:
        #     dic[n] -= 1
        #
        # for k in dic.keys():
        #     if dic[k] == 1:
        #         return k
        #
        # return None

        nums_set = set(nums)
        for n in range(len(nums) + 1):
            if n not in nums_set:
                return n

        return -1


if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(Solution().missingNumber(nums))
