# 3152. Special Array II

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix: list[int] = [0] * len(nums)
        prev: bool = nums[0] % 2 == 0  # even: True, odd: False
        for i in range(1, len(nums)):
            parity = nums[i] % 2 == 0
            if prev == parity:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]
            prev = parity

        ans: list[bool] = []
        for q in queries:
            ans.append(prefix[q[1]] == prefix[q[0]])
        return ans


ans = Solution().isArraySpecial([3, 4, 1, 2, 6], [[0, 4]])
print(ans)
