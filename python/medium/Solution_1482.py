# 1482. Minimum Number of Days to Make m Bouquets

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if self.checkBonquets(bloomDay, mid, m, k):
                right = mid
            else:
                left = mid + 1
        return left

    def checkBonquets(self, bloomDay, days, m, k):
        bonquets, flowers = 0, 0
        for bloom in bloomDay:
            if bloom > days:
                flowers = 0
            else:
                bonquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
        return bonquets >= m


bloomDay = [5, 5, 5, 7, 8, 9, 12, 7, 7]
m = 2
k = 3
ans = Solution().minDays(bloomDay, m, k)
print(ans)
