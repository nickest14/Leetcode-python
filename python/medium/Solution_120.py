# 120. Triangle


class Solution:
    def minimumTotal(self, triangle) -> int:
        level = len(triangle)
        dp = triangle[-1]
        # from bottom to top
        for layer in range(level - 2, -1, -1):
            for i in range(layer + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[layer][i]
        return dp[0]


ans = Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print(ans)
