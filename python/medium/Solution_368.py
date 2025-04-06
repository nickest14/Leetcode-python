# 368. Largest Divisible Subset

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n: int = len(nums)
        dp: list[int] = [1] * n
        max_size: int = 1
        max_index: int = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        ans: list[int] = []
        num = nums[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                ans.append(nums[i])
                num = nums[i]
                max_size -= 1
        return ans


ans = Solution().largestDivisibleSubset([1, 2, 4, 5, 8])
# ans = Solution().largestDivisibleSubset([1, 2, 3])
print(ans)
