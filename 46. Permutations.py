import time


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = []
        if not nums:
            return self.results
        self.search(sorted(nums), [], 0)
        return self.results

    def search(self, nums, S, index):
        if not nums:
            self.results.append(S)

        for i in range(len(nums)):
            self.search(nums[:i] + nums[i + 1:], S + [nums[i]], self.results)


if __name__ == "__main__":
    nums = [1, 2, 3]
    start = time.time()
    solution = Solution()
    print(solution.permute(nums))
    end = time.time()
    print("runtime = ", end - start)
