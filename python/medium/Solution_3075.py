# 3075. Maximize Happiness of Selected Children

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans: int = 0
        for i in range(k):
            val: int = happiness[i] - i
            if val > 0:
                ans += val
            else:
                break
        return ans


ans = Solution().maximumHappinessSum([1, 2, 3], 2)
print(ans)
