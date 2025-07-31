class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buy_price:
                if prices[i] - buy_price > max_profit:
                    max_profit = prices[i] - buy_price
            else:
                buy_price = prices[i]
        
        return max_profit
        