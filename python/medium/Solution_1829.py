# 1829. Maximum XOR for Each Query

from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        max_xor: int = (1 << maximumBit) - 1
        xor: int = nums[0]
        for i in range(1, n):
            xor ^= nums[i]

        ans: list[int] = []
        for i in range(n):
            ans.append(xor ^ max_xor)
            xor ^= nums[n - 1 - i]

        return ans


ans = Solution().getMaximumXor([2, 3, 4, 7], 3)
print(ans)
