# 3652. Best Time to Buy and Sell Stock using Strategy

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n: int = len(prices)
        h: int = k >> 1
        base = prev = nxt = 0

        for i in range(n):
            base += strategy[i] * prices[i]

        for i in range(k):
            prev += strategy[i] * prices[i]
            if i >= h:
                nxt += prices[i]

        best: int = max(0, nxt - prev)
        for right in range(k, n):
            left = right - k + 1
            prev += strategy[right] * prices[right] - strategy[left - 1] * prices[left - 1]
            nxt += prices[right] - prices[left - 1 + h]
            best = max(best, nxt - prev)

        return base + best


ans = Solution().maxProfit([4, 2, 8], [-1, 0, 1], 2)
print(ans)
