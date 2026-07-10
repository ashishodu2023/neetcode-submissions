class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0 

        min_price = float('inf')
        max_profit=0

        for price in prices:
            if price<min_price:
                min_price=price 

            current_profit = price - min_price
            max_profit = max(max_profit,current_profit)

        return max_profit
        