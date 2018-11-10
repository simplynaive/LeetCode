class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        return list({k: v for k, v in count.items() if v > len(nums) / 2}.keys())[0]



if __name__ == "__main__":
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))
