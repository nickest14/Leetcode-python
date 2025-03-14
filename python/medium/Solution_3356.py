# 3356. Zero Array Transformation II

from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n: int = len(nums)

        def can_make_zero_arr(k: int):
            diff: list[int] = [0] * (n + 1)
            for i in range(k):
                left, right, val = queries[i]
                diff[left] += val
                diff[right + 1] -= val

            curr_val = 0
            for i in range(n):
                curr_val += diff[i]
                if curr_val < nums[i]:
                    return False
            return True

        if all(x == 0 for x in nums):
            return 0

        left, right = 1, len(queries)

        if not can_make_zero_arr(right):
            return -1

        while left < right:
            mid = left + (right - left) // 2

            if can_make_zero_arr(mid):
                right = mid
            else:
                left = mid + 1

        return left


ans = Solution().minZeroArray([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]])


print(ans)
