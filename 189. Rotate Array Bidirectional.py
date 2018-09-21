import time


class Solution(object):
    def rotate(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or right == left:
            return
        if right > left:
            d = right - left
            nums[:] = nums[len(nums) - d:] + nums[:len(nums) - d]
        else:
            d = left - right
            nums[:] = nums[d:] + nums[:d]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    left = 7
    right = 5
    start = time.time()
    solution = Solution()
    solution.rotate(nums, left, right)
    print(nums)
    end = time.time()
    print("runtime = ", end - start)
