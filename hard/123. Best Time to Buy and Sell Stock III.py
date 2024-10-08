# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_days = len(prices)
        table = [0] * (total_days + 1)
        max_price = prices[-1]
        profit = 0
        for i in range(total_days - 1, -1, -1):
            max_price = max(max_price, prices[i])
            profit = max(profit, max_price - prices[i])
            table[i] = profit
        
        max_profit = 0
        cur_price = prices[0]
        for i, price in enumerate(prices):
            if price > cur_price:
                max_profit = max(max_profit, price - cur_price + table[i + 1])
            else:
                cur_price = price
        return max_profit
    
test = Solution()
print(test.maxProfit([3,3,5,0,0,3,1,4]))
print(test.maxProfit([1,2,3,4,5]))
print(test.maxProfit([7,6,4,3,1]))