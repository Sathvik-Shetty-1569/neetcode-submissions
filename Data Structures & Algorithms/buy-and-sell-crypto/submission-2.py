class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        amt = 0
        maxn = 0
        for l in range(len(prices)):
            for r in range(l,len(prices)):
                curr = prices[r]-prices[l]
                maxn = max(maxn,curr)
        
        return maxn
        
            

            