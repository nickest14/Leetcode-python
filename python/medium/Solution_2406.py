# 2406. Divide Intervals Into Minimum Number of Groups

from typing import List
import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ans: list[int] = []

        intervals.sort()
        for start, end in intervals:
            if ans and ans[0] < start:
                heapq.heappop(ans)
            heapq.heappush(ans, end)

        return len(ans)


ans = Solution().minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]])
print(ans)
