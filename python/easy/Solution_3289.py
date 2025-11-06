# 3289. The Two Sneaky Numbers of Digitville

from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        seen: list[bool] = [False] * n
        ans: list[int] = []
        for num in nums:
            if seen[num]:
                ans.append(num)
            else:
                seen[num] = True
        return ans


ans = Solution().getSneakyNumbers([0, 3, 2, 1, 3, 2])
print(ans)
