# 70. Climbing Stairs


class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1
        for _ in range(1, n):
            prev, curr = curr, prev + curr
        return curr


ans = Solution().climbStairs(4)
print(ans)
