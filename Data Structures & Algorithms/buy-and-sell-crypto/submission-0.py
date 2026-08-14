class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxd = 0

        for price in prices:
            if price < minp:
                minp = price
            if price - minp > maxd:
                maxd = price - minp
        
        return(maxd)

        