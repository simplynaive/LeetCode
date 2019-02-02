class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        nums.sort(reverse=True)
        self.top = nums[:k]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        left, right = 0, len(self.top)
        while left < right:
            mid = (left + right) // 2
            if val > self.top[mid]:
                right = mid
            else:
                left = mid + 1

        self.top.insert(left, val)
        if len(self.top) > self.k:
            self.top.pop()
        return self.top[-1]

# # Your KthLargest object will be instantiated and called as such:
#
#
# if __name__ == "__main__":
#     k = 3
#     nums = [4, 5, 8, 2]
#     obj = KthLargest(k, nums)
#     param_1 = obj.add(val)
#     print(Solution().hasCycle(t0))