class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1 
        maxp = float("-inf")
        while r < len(prices):
            buy = prices[r]
            sell = prices[r]
            prof = sell - prices[l]
            if buy < prices[l]:
                l = r
                
            elif prof > maxp:
                maxp = prof
                
            r+=1 
        
        if maxp == float("-inf"):
            return 0
        else:
            return maxp 
