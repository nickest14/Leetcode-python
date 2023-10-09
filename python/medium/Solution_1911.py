# 1911. Maximum Alternating Subsequence Sum

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sum_even, sum_odd = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            tmp_even = max(sum_odd + nums[i], sum_even)
            tmp_odd = max(sum_even - nums[i], sum_odd)
            sum_even, sum_odd = tmp_even, tmp_odd

        return sum_even

    # def maxAlternatingSum2(self, nums: List[int]) -> int:
    #     dp = {}

    #     # i = index, even = true / false
    #     def dfs(i, even):
    #         if i == len(nums):
    #             return 0
    #         if (i, even) in dp:
    #             return dp[(i, even)]

    #         total = nums[i] if even else (-1 * nums[i])
    #         dp[(i, even)] = max(total + dfs(i + 1, not even), dfs(i + 1, even))
    #         return dp[(i, even)]

    #     return dfs(0, True)


ans = Solution().maxAlternatingSum2([4, 2, 5, 3])
print(ans)
