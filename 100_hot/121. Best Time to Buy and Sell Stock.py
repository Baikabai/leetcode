class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = int(1e9)
        maxpro = 0
        for price in prices:
            maxpro = max(price-minprice,maxpro)
            minprice = min(price,minprice)
        return maxpro