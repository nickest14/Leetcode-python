# 2784. Check if Array is Good

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n: int = len(nums) - 1
        seen: set[int] = set()
        dup: bool = False

        for num in nums:
            if num > n:
                return False

            if num in seen:
                if num < n or dup:
                    return False
                dup = True
                continue

            seen.add(num)

        return True


ans = Solution().isGood([2, 1, 3])
print(ans)
