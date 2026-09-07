class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        res=0
        for r in range(1,len(prices)):
            if prices[r]>prices[r-1]:
                res+=prices[r]-prices[r-1]
        return res    