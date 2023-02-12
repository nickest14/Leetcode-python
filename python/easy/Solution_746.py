# 746. Min Cost Climbing Stairs

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
ans = Solution().minCostClimbingStairs(cost)
print(ans)
