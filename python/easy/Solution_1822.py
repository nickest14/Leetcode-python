# 1822. Sign of the Product of an Array

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = True
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                flag = not flag
        return 1 if flag else -1


ans = Solution().arraySign([-1, -2, -3, -4, 3, 2, 1])
print(ans)
