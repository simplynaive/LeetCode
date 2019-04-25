class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n, half = len(nums), sum(nums) // 2
        if sum(nums) & 1 or max(nums) > half:
            return False
        nums.sort(reverse=True)
        visited = {}

        def dfs(curr, i):
            if curr >= half: return curr == half
            if curr not in visited:
                visited[curr] = any(dfs(curr + nums[j], j) for j in range(i + 1, n))
            return visited[curr]

        return not nums or any(dfs(nums[i], i) for i in range(n))


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(Solution().canPartition(nums))
