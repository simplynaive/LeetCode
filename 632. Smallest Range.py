import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = []
        upper = nums[0][0]
        for i in range(len(nums)):
            pq.append((nums[i][0], i, 0))
            upper = max(nums[i][0], upper)
        import heapq
        heapq.heapify(pq)

        res = -float('inf'), float('inf')

        while pq:
            val, i, j = heapq.heappop(pq)
            if upper - val < res[1] - res[0]:
                res = val, upper
            if j == len(nums[i]) - 1:
                return res
            val = nums[i][j + 1]
            upper = max(val, upper)
            heapq.heappush(pq, (val, i, j + 1))


if __name__ == "__main__":
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(Solution().smallestRange(nums))
