# 904. Fruit Into Baskets

from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start: int = 0
        ans: int = 0
        fruit_count: defaultdict[int, int] = defaultdict(int)

        for end in range(len(fruits)):
            fruit_count[fruits[end]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1

            ans = max(ans, end - start + 1)

        return ans


ans = Solution().totalFruit([1, 2, 3, 2, 2])
print(ans)
