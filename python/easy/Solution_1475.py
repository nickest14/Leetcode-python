# 1475. Final Prices With a Special Discount in a Shop

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack: list = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)

        return prices


ans = Solution().finalPrices([8, 4, 6, 2, 3])
print(ans)
