# 3479. Fruits Into Baskets III

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n: int = len(baskets)
        s: int = 1

        while s < n:
            s *= 2

        tree: List[int] = [0] * (2 * s)
        for i in range(n):
            tree[s + i] = baskets[i]

        for i in range(s - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        unplaced_fruits: int = 0  
        for fruit in fruits:
            if tree[1] < fruit:
                unplaced_fruits += 1
                continue

            i = 1
            while i < s:  
                if tree[2 * i] >= fruit:
                    i = 2 * i
                else:
                    i = 2 * i + 1

            tree[i] = -1
            i //= 2

            while i > 0:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i //= 2

        return unplaced_fruits


ans = Solution().numOfUnplacedFruits([4, 2, 5], [3, 5, 4])
print(ans)
