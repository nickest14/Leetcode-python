# 135. Candy

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n: int = len(ratings)
        candy: list[int] = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candy[i] = candy[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)


ans = Solution().candy([1, 0, 2])
print(ans)
