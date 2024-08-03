# 2134. Minimum Swaps to Group All 1's Together II

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        mx = cnt = sum(nums[:k])
        n = len(nums)
        for i in range(k, n + k):
            # new slide window's right
            cnt += nums[i % n]
            # oid slide window's right
            cnt -= nums[(i - k + n) % n]
            mx = max(mx, cnt)
        return k - mx


# ans = Solution().minSwaps([0, 1, 0, 1, 1, 0, 0])
ans = Solution().minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0])
print(ans)
