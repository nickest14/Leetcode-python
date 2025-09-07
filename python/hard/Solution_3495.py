# 3495. Minimum Operations to Make Array Elements Zero

from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans: int = 0
        for query in queries:
            left, right = query
            total_steps: int = 0
            layer_start: int = 1
            layer_depth: int = 1
            while layer_start <= right:
                start: int = max(left, layer_start)
                end: int = min(right, layer_start * 4 - 1)
                if end >= start:
                    total_steps += (end - start + 1) * layer_depth
                layer_start *= 4
                layer_depth += 1
            ans += (total_steps // 2) + (total_steps % 2)
        return ans


ans = Solution().minOperations([[1, 2], [2, 4]])
print(ans)
