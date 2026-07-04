class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        max_profit = 0
        min_profit = float("inf")

        for price in prices:
            if price < min_profit:
                min_profit = price

            else:
                current_profit = price - min_profit
                max_profit = max(max_profit, current_profit)

        return max_profit
