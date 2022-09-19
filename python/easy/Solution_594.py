# 594. Longest Harmonious Subsequence

from typing import List
import collections


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter, longest = collections.Counter(nums), 0
        for num in nums:
            if num + 1 in counter:
                longest = max(longest, counter[num] + counter[num + 1])
        return longest


ans = Solution().findLHS([3, 2, 2, 2])
print(ans)
