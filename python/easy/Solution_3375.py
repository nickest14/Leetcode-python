# 3375. Minimum Operations to Make Array Values Equal to K

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        visited = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                visited.add(num)
        return len(visited)


ans = Solution().minOperations([5, 2, 5, 4, 5], 2)
print(ans)
