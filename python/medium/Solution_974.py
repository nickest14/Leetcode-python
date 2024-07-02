# 974. Subarray Sums Divisible by K

from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod in prefix_map:
                count += prefix_map[mod]

            prefix_map[mod] += 1

        return count


# ans = Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5)
ans = Solution().subarraysDivByK([-2, -3, 1], 5)
print(ans)
