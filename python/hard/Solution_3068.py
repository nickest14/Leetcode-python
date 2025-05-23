# 3068. Find the Maximum Sum of Node Values

from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        base: int = sum(nums)
        sum_pos = cnt_pos = 0
        min_pos: int = float('inf')
        best_nonpos: int = float('-inf')

        for x in nums:
            d = (x ^ k) - x
            if d > 0:
                cnt_pos += 1
                sum_pos += d
                min_pos = min(min_pos, d)
            else:
                best_nonpos = max(best_nonpos, d)

        if cnt_pos % 2 == 0:
            return base + sum_pos

        loss = min(min_pos, -best_nonpos)
        return base + sum_pos - loss


ans = Solution().maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]])
print(ans)
