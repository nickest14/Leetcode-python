# 2099. Find Subsequence of Length K With the Largest Sum

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n: int = len(nums)
        values: List[tuple[int, int]] = [(i, nums[i]) for i in range(n)]
        values.sort(key=lambda x: x[1], reverse=True)
        values = sorted(values[:k], key=lambda x: x[0])

        ans: List[int] = [val for _, val in values]
        return ans


ans = Solution().maxSubsequence([2, 1, 3, 3], 2)
print(ans)
