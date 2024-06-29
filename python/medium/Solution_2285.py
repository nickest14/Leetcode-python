# 2285. Maximum Total Importance of Roads

from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        cost = 1
        count = [0] * n
        for road in roads:
            count[road[0]] += 1
            count[road[1]] += 1

        count.sort()
        for c in count:
            ans += c * cost
            cost += 1

        return ans


n = 5
roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
# roads = [[0, 3], [2, 4], [1, 3]]
ans = Solution().maximumImportance(n, roads)
print(ans)
