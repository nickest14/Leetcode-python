# 1411. Number of Ways to Paint N × 3 Grid

from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo: dict[tuple[int, int], int] = {}

        def dp(i: int, j: int) -> int:
            if i == len(nums1) or j == len(nums2):
                return float("-inf")

            if (i, j) in memo:
                return memo[(i, j)]

            take = nums1[i] * nums2[j]
            value = max(
                take + dp(i + 1, j + 1),
                take,
                dp(i + 1, j),
                dp(i, j + 1),
            )

            memo[(i, j)] = value

            return memo[(i, j)]

        return dp(0, 0)


ans = Solution().maxDotProduct([2, 1, -2, 5], [3, 0, -6])
print(ans)
