import time
import copy

class Solution:
    # recursive method
    # def search(self, nums, S, index):
    #     if index == len(nums):
    #         self.results.append(S)
    #         return
    #
    #     self.search(nums, S + [nums[index]], index + 1)
    #     self.search(nums, S, index + 1)
    #
    # def subsets(self, nums):
    #     self.results = []
    #     if not nums:
    #         return self.results
    #     self.search(sorted(nums), [], 0)
    #     return self.results

    # non-recursive method
    def subsets(self, nums):
        nums.sort()
        self.results = [[]]
        for i in range(len(nums)):
            m = copy.deepcopy(self.results)
            for t in m:
                t += [nums[i]]
            self.results.extend(m)
        return self.results


if __name__ == "__main__":
    nums = [1, 2, 3]
    start = time.time()
    solution = Solution()
    print(solution.subsets(nums))
    end = time.time()
    print("runtime = ", end - start)
