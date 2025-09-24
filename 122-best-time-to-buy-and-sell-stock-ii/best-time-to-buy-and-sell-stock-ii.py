class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        curr_profit = 0
        total_profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] >= prices[i]:
                curr_profit = prices[i + 1] - min_price
            else:
                total_profit += curr_profit
                min_price = prices[i + 1]
                curr_profit = 0
        
        return total_profit + curr_profit
