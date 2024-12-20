# 769. Max Chunks To Make Sorted

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans: int = 0
        max_so_far = arr[0]

        for i in range(len(arr)):
            if max_so_far < arr[i]:
                max_so_far = arr[i]

            if max_so_far == i:
                ans += 1

        return ans


ans = Solution().maxChunksToSorted([1, 0, 2, 4, 3])
print(ans)
