# 3740. Minimum Distance Between Three Equal Elements I

from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp: dict[int, list[int]] = defaultdict(list)
        n: int = len(nums)

        for i in range(n):
            mp[nums[i]].append(i)

        ans: int = float("inf")

        for indices in mp.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i + 2] - indices[i])
                ans = min(ans, dist)

        return -1 if ans == float("inf") else ans


ans = Solution().minimumDistance([1, 2, 1, 1, 3])
print(ans)
