class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        dp = []
        min = float("inf")
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            dp.append(prices[i] - min)
        return max(max(dp), 0)


if __name__ == "__main__":
    prices = [1, 2]
    print(Solution().maxProfit(prices))
