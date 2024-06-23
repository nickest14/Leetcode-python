# 3191. Minimum Operations to Make Binary Array Elements Equal to One I

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] != 1:
                ans += 1
                for j in range(i, i + 3):
                    nums[j] = 1 if nums[j] == 0 else 0

        return ans if all(nums) else -1


ans = Solution().minOperations([0, 1, 1, 1, 0, 0])
print(ans)
