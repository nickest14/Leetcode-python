# 3347. Maximum Frequency of an Element After Performing Operations II

from typing import List
from collections import Counter, defaultdict


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq: Counter = Counter(nums)
        presum: defaultdict[int, int] = defaultdict(int)
        for freq_key in freq:
            presum[freq_key - k] += freq[freq_key]
            presum[freq_key + k + 1] -= freq[freq_key]
        keys = sorted(presum.keys() | freq.keys())


        ans: int = 0
        total: int = 0
        for key in keys:
            total += presum[key]
            ops: int = min(
                total - freq[key], numOperations
            )
            ans = max(ans, freq[key] + ops)
        return ans


ans = Solution().maxFrequency([88, 53], 27, 2)
print(ans)

# ans = Solution().maxFrequency([5, 64], 42, 2)
# print(ans)
