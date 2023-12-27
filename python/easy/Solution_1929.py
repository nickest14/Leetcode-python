# 1929. Concatenation of Array

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):
            for num in nums:
                ans.append(num)
        return ans


ans = Solution().getConcatenation(1, 2, 1)
print(ans)
