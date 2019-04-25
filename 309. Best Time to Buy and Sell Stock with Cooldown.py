class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        hold - ----do nothing - ---->hold
        hold - ----sell - ----> notHold_cooldown
        notHold - ----do nothing - ----> notHold
        notHold - ----buy - ----> hold
        notHold_cooldown - ----do nothing - ---->notHold
        '''
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(prices))

'''
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''
