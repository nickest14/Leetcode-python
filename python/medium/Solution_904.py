# 904. Fruit Into Baskets

from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l, total, ans = 0, 0, 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1
                if not count[f]:
                    count.pop(f)

            ans = max(ans, total)
        return ans


ans = Solution().totalFruit([1, 2, 3, 2, 2])
print(ans)
