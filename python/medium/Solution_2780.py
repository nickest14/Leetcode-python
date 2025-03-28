# 2780. Minimum Index of a Valid Split

from typing import List
from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq: dict[int, int] = Counter(nums)
        dominant: int = 0
        count: int = 0
        for num, c in freq.items():
            if c > len(nums) // 2:
                dominant = num
                count = c
                break

        left_count: int = 0
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left_count += 1
            left_size = i + 1
            right_size = len(nums) - left_size
            right_count = count - left_count

            if left_count > left_size // 2 and right_count > right_size // 2:
                return i

        return -1


ans = Solution().minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1])
print(ans)
