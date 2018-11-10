class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            if profit > 0:
                sum += profit
        return sum


if __name__ == "__main__":
    nums = [7, 1, 5, 3, 4, 6]
    print(Solution().maxProfit(nums))
