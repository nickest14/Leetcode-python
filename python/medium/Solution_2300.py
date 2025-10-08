# 2300. Successful Pairs of Spells and Potions

from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        ans: list[int] = []
        for spell in spells:
            left: int = 0
            right: int = len(potions) - 1
            while left <= right:
                mid: int = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(len(potions) - left)
        return ans


ans = Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16)
print(ans)
