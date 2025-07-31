# 2044. Count Number of Maximum Bitwise-OR Subsets

from typing import List


class Solution:
    def __init__(self):
        self.count: int = 0
        self.max_or: int = 0
        self.nums: list[int] = []

    def backtrack(self, index: int, current_or: int):
        if current_or == self.max_or:
            self.count += 1
        for i in range(index, len(self.nums)):
            new_or = current_or | self.nums[i]
            if new_or <= self.max_or:
                self.backtrack(i + 1, new_or)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.nums = nums
        for num in nums:
            self.max_or |= num

        self.backtrack(0, 0)
        return self.count


# ans = Solution().countMaxOrSubsets([3, 1])
ans = Solution().countMaxOrSubsets([3, 2, 1, 5])
print(ans)
