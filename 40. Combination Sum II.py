class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, start, combination, results):
        if target == 0 and list(combination) not in results:
            return results.append(list(combination))
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return

            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i + 1, combination, results)
            combination.pop()


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))
