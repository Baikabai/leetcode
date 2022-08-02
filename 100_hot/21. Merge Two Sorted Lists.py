class Solution:
    def maxProfit(self, prices) -> int:
        minprice = int(1e9)
        maxpro = 0
        for price in prices:
            maxpro = max(price-minprice,maxpro)
            minprice = min(price,minprice)
            print(maxpro,minprice)
        
        return maxpro

print(Solution.maxProfit('a',[1,7,5,3,6,4]))