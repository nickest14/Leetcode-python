# 2200. Find All K-Distant Indices in an Array

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans: list[int] = []
        n: int = len(nums)
        right: int = 0

        for i, num in enumerate(nums):
            if num == key:
                left: int = max(right, i - k)
                right: int = min(n, i + k + 1)
                ans.extend(range(left, right))

        return ans


ans = Solution().findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1)
print(ans)
