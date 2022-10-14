# 122. Best Time to Buy and Sell Stock II

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for prev, curr in zip(prices, prices[1:]):
            if (val := curr - prev) > 0:
                sum += val
        return sum


ans = Solution().maxProfit([7, 1, 5, 3, 6, 4])
print(ans)
