# 2593. Find Score of an Array After Marking All Elements

from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans: int = 0
        seen = set()
        n: int = len(nums)
        queue = sorted(enumerate(nums), key=lambda x: (x[1], x[0]))

        for idx, num in queue:
            if idx in seen:
                continue
            ans += num
            seen.add(idx)
            if idx > 0:
                seen.add(idx - 1)
            if idx < n - 1:
                seen.add(idx + 1)

        return ans


ans = Solution().findScore([2, 1, 3, 4, 5, 2])
print(ans)
