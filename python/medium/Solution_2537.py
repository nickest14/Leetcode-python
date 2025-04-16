# 2537. Count the Number of Good Subarrays

from typing import List
from collections import defaultdict


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans: int = 0
        freq: defaultdict[int, int] = defaultdict(int)
        pairs: int = 0
        left: int = 0
        n: int = len(nums)

        for right in range(n):
            val: int = nums[right]
            pairs += freq[val]
            freq[val] += 1
            while pairs >= k:
                ans += n - right
                out = nums[left]
                freq[out] -= 1
                pairs -= freq[out]
                left += 1
        return ans


# ans = Solution().countGood([1, 1, 1, 1, 1], 10)
# ans = Solution().countGood([3, 1, 4, 3, 2, 2, 4], 2)
ans = Solution().countGood([1,2,3,4,5,6,1, 8,9,10], 1)
print(ans)
