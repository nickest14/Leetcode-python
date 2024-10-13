# 632. Smallest Range Covering Elements from K Lists

from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n: int = len(nums)
        pq: list[int] = []
        ma = float('-inf')
        for i in range(n):
            heapq.heappush(pq, (nums[i][0], i, 0))
            ma = max(ma, nums[i][0])

        ans = [pq[0][0], ma]
        while True:
            _, i, j = heapq.heappop(pq)
            if j == len(nums[i]) - 1:
                break
            next_num: int = nums[i][j + 1]
            ma = max(ma, next_num)
            heapq.heappush(pq, (next_num, i, j + 1))

            if ma - pq[0][0] < ans[1] - ans[0]:
                ans = [pq[0][0], ma]

        return ans


ans = Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
# ans = Solution().smallestRange([[0, 5, 9], [15, 16]])
print(ans)
