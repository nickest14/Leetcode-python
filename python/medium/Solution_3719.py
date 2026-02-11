# 3719. Longest Balanced Subarray I

from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n: int = len(nums)
        ans: int = 0

        seen: list[int] = [0] * (max(nums) + 1)

        for i in range(n):
            if n - i <= ans:
                break

            distinct_even_odd: list[int] = [0, 0]  # [distinct evens, distinct odds]
            for j in range(i, n):
                val = nums[j]
                if seen[val] != i + 1:
                    seen[val] = i + 1
                    distinct_even_odd[val & 1] += 1

                if distinct_even_odd[0] == distinct_even_odd[1]:
                    ans = max(ans, j - i + 1)

        return ans


ans = Solution().longestBalanced([2, 5, 4, 3])
print(ans)
