class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0

        for right in range(1, len(prices)):

            while prices[left] > prices[right] and left < right:
                left += 1
            
            max_profit = max(max_profit, prices[right] - prices[left])
        
        return max_profit

