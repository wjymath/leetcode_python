class Solution(object):
    def maxProfit(prices):
        min_seen, max_profit = float('inf'), 0
        for p in prices:
            min_seen = min(min_seen, p)
            curr_profit = p - min_seen
            max_profit = max(curr_profit, max_profit)
        return max_profit

print(Solution().maxProfit([10000,9999,9998,9997,9996,9995,9994,9993,9992,9991,9990,9989,9988,9987,9986,9985,9984,9983,9982,9981,9980,9979]))