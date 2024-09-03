# 1894. Find the Student that Will Replace the Chalk

from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remain: int = k % sum(chalk)
        for index, c in enumerate(chalk):
            if remain < c:
                return index
            remain -= c

    # # Binary search
    # def chalkReplacer(self, chalk: List[int], k: int) -> int:
    #     # Calculate the prefix
    #     for c in range(1, len(chalk)):
    #         chalk[c] += chalk[c - 1]

    #     remain: int = k % chalk[-1]
    #     left: int = 0
    #     right: int = len(chalk) - 1
    #     while left < right:
    #         mid: int = left + (right - left) // 2
    #         if remain > chalk[mid]:
    #             left = mid + 1
    #         elif remain == chalk[mid]:
    #             return mid + 1
    #         else:
    #             right = mid
    #     return left


ans = Solution().chalkReplacer([5, 1, 5], 22)
# ans = Solution().chalkReplacer([1, 4, 5, 6], 10)
print(ans)
