class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # import heapq
        # nums = list(set(nums))
        # if len(nums) < 3:
        #     return max(nums)
        # num_heap = nums[:3]
        # heapq.heapify(num_heap)
        #
        # for n in nums[3:]:
        #     if num_heap[0] < n:
        #         heapq.heappop(num_heap)
        #         heapq.heappush(num_heap, n)
        #
        # return num_heap[0]

        # one-pass
        res = [-float('inf')] * 3
        for n in nums:
            if n not in res:
                if n > res[2]:
                    res = [res[1], res[2], n]
                elif n > res[1]:
                    res = [res[1], n, res[2]]
                elif n > res[0]:
                    res = [n, res[1], res[2]]
            print(res)
        if -float('inf') in res:
            return max(nums)
        return res[0]


if __name__ == "__main__":
    nums = [3, 2]
    print(Solution().thirdMax(nums))
