# 2845. Count of Interesting Subarrays

from typing import List
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans: int = 0
        prefix_mod: int = 0
        mod_freq: dict[int, int] = defaultdict(int)
        mod_freq[0] = 1
        for num in nums:
            if num % modulo == k:
                prefix_mod = (prefix_mod + 1) % modulo

            needed = (prefix_mod - k) % modulo
            ans += mod_freq.get(needed, 0)

            mod_freq[prefix_mod] += 1
        return ans


ans = Solution().countInterestingSubarrays([3, 2, 4, 7, 1], 2, 1)
print(ans)
