# 747. Largest Number At Least Twice of Others

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, second, index = -1, -1, -1
        for ind, num in enumerate(nums):
            if num > largest:
                largest, second = num, largest
                index = ind
            elif num > second:
                second = num
        return index if largest >= 2 * second else -1


ans = Solution().dominantIndex([3, 6, 1, 0])
print(ans)
