# 2078. Two Furthest Houses With Different Colors

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n: int = len(colors)
        left, right = 0, n - 1

        for i in range(n):
            if colors[i] ^ colors[-1]:
                left = i
                break

        for i in range(n - 1, -1, -1):
            if colors[i] ^ colors[0]:
                right = i
                break

        return max(n - 1 - left, right)


ans = Solution().maxDistance([1, 1, 1, 6, 1, 1, 1])
print(ans)
