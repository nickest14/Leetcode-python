# 1863. Sum of All Subset XOR Totals

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i: int, xor: int) -> int:
            if i == len(nums):
                return xor

            include_num = dfs(i + 1, xor ^ nums[i])
            exclude_num = dfs(i + 1, xor)
            return include_num + exclude_num

        return dfs(0, 0)


ans = Solution().subsetXORSum([1, 3])
# ans = Solution().subsetXORSum([1, 2, 3])
print(ans)
