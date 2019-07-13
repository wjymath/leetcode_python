class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i - 1])

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5,6]))