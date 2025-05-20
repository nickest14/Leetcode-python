# 3355. Zero Array Transformation I

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n: int = len(nums)
        delta: list[int] = [0] * (n + 1)
        for left, right in queries:
            delta[left] += 1
            if right + 1 < n:
                delta[right + 1] -= 1

        new_delta: list[int] = [0] * n
        new_delta[0] = delta[0]
        for i in range(1, n):
            new_delta[i] = delta[i] + new_delta[i - 1]

        for i in range(n):
            if nums[i] - new_delta[i] > 0:
                return False
        return True


ans = Solution().isZeroArray([1, 0, 1], [[0, 2]])
# ans = Solution().isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]])
print(ans)
