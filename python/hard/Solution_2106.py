# 2106. Maximum Fruits Harvested After at Most K Steps

from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = total = ans = 0
        for right in range(len(fruits)):
            total += fruits[right][1]
            while (
                left <= right
                and min(
                    abs(startPos - fruits[left][0])
                    + fruits[right][0]
                    - fruits[left][0],
                    abs(startPos - fruits[right][0])
                    + fruits[right][0]
                    - fruits[left][0],
                )
                > k
            ):
                total -= fruits[left][1]
                left += 1
            ans = max(ans, total)
        return ans


ans = Solution().maxTotalFruits([[2, 8], [6, 3], [8, 6]], 5, 4)
print(ans)
