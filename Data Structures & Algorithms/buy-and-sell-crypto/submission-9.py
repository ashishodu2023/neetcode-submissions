class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        left = 0
        right = 1

        max_profit = 0

        for right in range(len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right

        return max_profit
