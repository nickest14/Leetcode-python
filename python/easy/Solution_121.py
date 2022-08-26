# 121. Best Time to Buy and Sell Stock

from typing import List
import operator


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_here, max_profit = 0, 0
        for profit in map(operator.sub, prices[1:], prices):
            max_here = max(max_here + profit, 0)
            max_profit = max(max_profit, max_here)
        return max_profit


# ans = Solution().maxProfit([15, 3, 6, 1, 8, 10])
ans = Solution().maxProfit([7, 1, 5, 3, 6, 7, 4])
print(ans)
