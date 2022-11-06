# 1051. Height Checker

from typing import List
import collections


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = collections.Counter(heights)
        count, curr = 0, 1
        for height in heights:
            while counter[curr] == 0:
                curr += 1
            count += (curr != height)
            counter[curr] -= 1
        return count


ans = Solution().heightChecker([1, 1, 4, 2, 1, 3])
print(ans)
