# 3477. Fruits Into Baskets II

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used_baskets: List[bool] = [False] * len(baskets)
        unplaced_fruits: int = 0
        for fruit in fruits:
            placed: bool = False
            for i in range(len(baskets)):
                if not used_baskets[i] and fruit <= baskets[i]:
                    used_baskets[i] = True
                    placed = True
                    break
            if not placed:
                unplaced_fruits += 1

        return unplaced_fruits


ans = Solution().numOfUnplacedFruits([4, 2, 5], [3, 5, 4])
print(ans)
