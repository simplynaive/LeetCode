import time

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or not amount:
            return 0
        inf = float("inf")
        dp = [inf] * (amount + 1)
        dp[0] = 0
        coins = sorted(coins, reverse=True)
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] < inf:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == inf:
            return -1
        else:
            return dp[amount]


if __name__ == "__main__":
    coins = [205, 37, 253, 463, 441, 129, 156, 429, 101, 423, 311]
    amount = 6653
    start = time.time()
    print(Solution().coinChange(coins, amount))
    print(time.time() - start)
