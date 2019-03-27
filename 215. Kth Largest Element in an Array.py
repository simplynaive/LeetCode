class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        num_heap = nums[:k]
        heapq.heapify(num_heap)
        for n in nums[k:]:
            if num_heap[0] < n:
                heapq.heappop(num_heap)
                heapq.heappush(num_heap, n)

        return num_heap[0]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 4
    print(Solution().findKthLargest(nums, k))
