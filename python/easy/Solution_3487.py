# 3487. Maximum Unique Subarray Sum After Deletion

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        min_val: int = float("-inf")
        seen: set = set()
        ans: int = 0

        for val in nums:
            if val not in seen:
                if val >= 0:
                    ans += val
                else:
                    min_val = max(min_val, val)

            seen.add(val)

        if ans == 0 and 0 not in seen:
            return min_val

        return ans


ans = Solution().maxSum([1, -2, 0, 3, -4])
print(ans)
