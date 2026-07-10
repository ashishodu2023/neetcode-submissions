"""
Sliding Window Solutiom

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0 
        
        left = 0 
        max_profit = 0 

        for right in range(len(prices)):
            if prices[left]<prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right
        return max_profit
           
            
        