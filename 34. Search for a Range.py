import time

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # sequential search
        # if not nums:
        #     return [-1, -1]
        # start, end = 0, 0
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         start = i
        #         for j in range(i, len(nums)):
        #             if nums[j] == target:
        #                 end = j
        #         return [start, end]
        # return [-1, -1]

        # binary search
        self.result = [-1, -1]
        if not nums:
            return self.result
        start, end = 0, len(nums) - 1
        while start < end:
            mid = int((start + end) / 2)
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if nums[start] != target:
            return self.result
        self.result[0] = start
        end = len(nums) - 1
        while start < end:
            mid = int((start + end) / 2) + 1
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        self.result[1] = end
        return self.result


if __name__ == "__main__":
    nums = [1, 3]
    target = 1
    start = time.time()
    solution = Solution()
    print(solution.searchRange(nums, target))
    end = time.time()
    print("runtime = ", end - start)
