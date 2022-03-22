class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 1:
            return 0
        buyIndex = 0
        sellIndex = 0
        profit = []
        for i in range(l):
            if prices[buyIndex] > prices[i]:
                buyIndex = i
                sellIndex = i
            if prices[sellIndex] < prices[i]:
                sellIndex = i
            if buyIndex <= sellIndex:
                profit.append(prices[sellIndex]-prices[buyIndex])
        return max(profit)