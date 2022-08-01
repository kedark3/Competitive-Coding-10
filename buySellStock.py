# Approach: Two pointers
# TC O(N)
# SC O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,h = 0, 1  # buy,sell pointers
        maxP = 0 # maxProfit
        while h < len(prices):
            if prices[l] < prices[h]:
                profit = prices[h] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = h
            h += 1
        return maxP