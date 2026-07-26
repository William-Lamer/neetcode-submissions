class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            min_buy = min(min_buy, sell)
            max_profit = max(max_profit, sell - min_buy)
            

        return max_profit