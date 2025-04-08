# 3396. Minimum Number of Operations to Make Elements in Array Distinct

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        map: list[int] = [0] * 101

        for i in range(len(nums) - 1, -1, -1):
            map[nums[i]] += 1
            if map[nums[i]] == 2:
                return (i + 3) // 3
        return 0


ans = Solution().minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7])
print(ans)
