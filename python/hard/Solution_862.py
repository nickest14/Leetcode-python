# 862. Shortest Subarray with Sum at Least K

from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q: deque[tuple[int, int]] = deque([(0, 0)])
        ans, cur = float('inf'), 0
        for i, num in enumerate(nums):
            cur += num
            while q and cur - q[0][1] >= k:
                ans = min(ans, i + 1 - q.popleft()[0])
            while q and cur <= q[-1][1]:
                q.pop()
            q.append((i + 1, cur))

        return ans if ans < float('inf') else -1


ans = Solution().shortestSubarray([1, 2, 3, 4, 5], 7)
# ans = Solution().shortestSubarray([0, 0, 1, 2, 5, -1, 6], 10)
print(ans)
