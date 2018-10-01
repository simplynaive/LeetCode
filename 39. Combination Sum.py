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
        if target == 0:
            return results.append(list(combination))

        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return

            combination.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, combination, results)
            combination.pop()


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
