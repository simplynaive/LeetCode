class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        if len(costs) == 1:
            return min(costs[0])
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][1], costs[i - 1][0])
        return min(costs[-1])


if __name__ == "__main__":
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    print(Solution().minCost(costs))
