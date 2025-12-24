# 3074. Apple Redistribution into Boxes

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)

        ans: int = 0
        for cap in capacity:
            total -= cap
            ans += 1
            if total <= 0:
                return ans
        return ans


ans = Solution().minimumBoxes([1, 3, 2], capacity=[4, 3, 1, 5, 2])
print(ans)
