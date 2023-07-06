# 11. Container With Most Water

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        h = max(height)

        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1

            if (r - l) * h <= ans:
                break
        return ans


ans = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(ans)
