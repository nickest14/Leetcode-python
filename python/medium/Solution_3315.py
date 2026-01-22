# 3315. Construct the Minimum Bitwise Array II

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans: list[int] = []
        for num in nums:
            if num & 1:
                bit = ((num + 1) & ~num) >> 1
                ans.append(num & ~bit)
            else:
                ans.append(-1)

        return ans


ans = Solution().minBitwiseArray([2, 3, 5, 7])
print(ans)
