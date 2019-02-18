class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums:
            self.sums = [0]
            self.sums[0] = nums[0]
            for i in range(1, len(nums)):
                self.sums.append(self.sums[i - 1] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == "__main__":
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    print(NumArray().sumRange(n, k))