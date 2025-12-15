# 2110. Number of Smooth Descent Periods of a Stock

from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans: int = 0
        count: int = 1
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                count += 1
            else:
                ans += (count * (count + 1)) // 2
                count = 1
        ans += (count * (count + 1)) // 2
        return ans


ans = Solution().getDescentPeriods([3, 2, 1, 4])
print(ans)
