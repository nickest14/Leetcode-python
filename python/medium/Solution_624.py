# 624. Maximum Distance in Arrays

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value: int = arrays[0][0]
        max_value: int = arrays[0][-1]
        ans: int = 0
        for array in arrays[1:]:
            ans = max(ans, max_value - array[0], array[-1] - min_value)
            min_value = min(min_value, array[0])
            max_value = max(max_value, array[-1])

        return ans


ans = Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]])
# ans = Solution().maxDistance([[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]])
print(ans)
