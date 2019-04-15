import time
import copy

class Solution:
    # recursive method
    def subsets(self, nums):
        res = []
        if not nums:
            return res
        self.dfs(sorted(nums), [], 0, res)
        return res

    def dfs(self, nums, path, index, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, path + [nums[i]], i + 1, res)

    # # non-recursive method
    # def subsets(self, nums):
    #     nums.sort()
    #     self.results = [[]]
    #     for i in range(len(nums)):
    #         m = copy.deepcopy(self.results)
    #         for t in m:
    #             t += [nums[i]]
    #         self.results.extend(m)
    #     return self.results


if __name__ == "__main__":
    nums = [1, 2, 3]
    start = time.time()
    solution = Solution()
    print(solution.subsets(nums))
    end = time.time()
    print("runtime = ", end - start)
