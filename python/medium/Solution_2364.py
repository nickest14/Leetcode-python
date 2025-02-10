# 2364. Count Number of Bad Pairs

from typing import List
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diff_count: dict[int, int] = defaultdict(int)
        bad_pairs: int = 0

        for i in range(len(nums)):
            val: int = nums[i] - i
            good_pairs = diff_count[val]
            bad_pairs += i - good_pairs
            diff_count[val] += 1

        return bad_pairs


ans = Solution().countBadPairs([4, 1, 3, 3])
# ans = Solution().countBadPairs([2, 3, 4, 5])
print(ans)
