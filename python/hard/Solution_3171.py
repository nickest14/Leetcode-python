# 3171. Find Subarray With Bitwise OR Closest to K

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        dp = set()
        cur = {0}
        for num in nums:
            cur = {x | num for x in cur} | {num}
            dp |= cur

        ans = float('inf')
        for x in dp:
            ans = min(ans, abs(k - x))
        return ans

# ans = Solution().minimumDifference([1, 2, 4, 5], 3)
# ans = Solution().minimumDifference([1, 3, 1, 3], 2)
ans = Solution().minimumDifference([1,2,3], 2)
print(ans)


# 1: 001
# 2: 010
# 3: 011
# 4: 100
# 5: 101