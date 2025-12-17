# 3573. Best Time to Buy and Sell Stock V

from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        profit: list[int] = [0] * (k + 1)
        buy: list[int] = [float("-inf")] * (k + 1)
        sell: list[int] = [float("-inf")] * (k + 1)
        for price in prices:
            prev = profit[0]
            for i in range(1, k + 1):
                p = profit[i]
                profit[i] = max(profit[i], buy[i] + price, sell[i] - price)
                buy[i] = max(buy[i], prev - price)
                sell[i] = max(sell[i], prev + price)
                prev = p
        return max(profit)


ans = Solution().maximumProfit([1, 7, 9, 8, 2], 2)
print(ans)
