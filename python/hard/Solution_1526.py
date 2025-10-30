# 1526. Minimum Number of Increments on Subarrays to Form a Target Array

from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans: int = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                ans += target[i] - target[i - 1]
        return ans


ans = Solution().minNumberOperations([1, 2, 3, 2, 1])
print(ans)
