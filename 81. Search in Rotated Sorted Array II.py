import time


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return True
            if nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[start] > nums[mid]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                start += 1

        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False


if __name__ == "__main__":
    nums = [1, 1, 3, 1]
    target = 3

    start = time.time()
    solution = Solution()
    print(solution.search(nums, target))
    end = time.time()
    print("runtime = ", end - start)
