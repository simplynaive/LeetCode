class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


if __name__ == "__main__":
    coins = [205, 37, 253, 463, 441, 129, 156, 429, 101, 423, 311]
    amount = 6653
    print(Solution().coinChange(coins, amount))
