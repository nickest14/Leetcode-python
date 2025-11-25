# 1018. Binary Prefix Divisible By 5

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans: list[bool] = []
        val: int = 0
        for num in nums:
            val = val * 2 + num
            ans.append(val % 5 == 0)
        return ans


ans = Solution().prefixesDivBy5([0, 1, 1])
print(ans)
