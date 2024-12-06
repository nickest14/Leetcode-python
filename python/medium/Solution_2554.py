# 2554. Maximum Number of Integers to Choose From a Range I

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans: int = 0
        banned = set(banned)
        total_sum: int = 0
        for i in range(1, n + 1):
            if i in banned:
                continue
            total_sum += i
            if total_sum > maxSum:
                break
            ans += 1

        return ans


ans = Solution().maxCount([1, 6, 5], 5, 6)
print(ans)
