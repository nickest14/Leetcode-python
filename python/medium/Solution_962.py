# 962. Maximum Width Ramp

from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr: list[tuple[int, int]] = sorted([(num, i) for i, num in enumerate(nums)])
        ans: int = 0
        min_index: int = float('inf')
        for _, i in arr:
            ans = max(ans, i - min_index)
            min_index = min(min_index, i)

        return ans


# ans = Solution().maxWidthRamp([6, 0, 8, 2, 1, 5])
ans = Solution().maxWidthRamp([1, 0])
print(ans)
