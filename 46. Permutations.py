import time


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []

        def dfs(nums, path):
            if not nums:
                res.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        dfs(nums, [])
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    start = time.time()
    solution = Solution()
    print(solution.permute(nums))
    end = time.time()
    print("runtime = ", end - start)
