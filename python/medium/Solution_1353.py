# 1353. Maximum Number of Events That Can Be Attended

from typing import List
from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap: list[int] = []
        i: int = 0
        n: int = len(events)
        ans: int = 0

        last_day: int = max(end for _, end in events)

        for day in range(1, last_day + 1):
            while i < n and events[i][0] == day:
                heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heappop(min_heap)

            if min_heap:
                heappop(min_heap)
                ans += 1

            if i == n and not min_heap:
                break

        return ans


ans = Solution().maxEvents([[1,2],[2,3],[3,4]])
print(ans)
