# 2551. Put Marbles in Bags

from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        pair_sums: list[int] = []
        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i + 1])

        pair_sums.sort()
        min_scores: int = sum(pair_sums[: k - 1])
        max_scores: int = sum(pair_sums[-(k - 1) :])
        return max_scores - min_scores


ans = Solution().putMarbles([1, 3, 5, 1], 2)
# ans = Solution().putMarbles([1,10,8,3,3,3,2], 2)
print(ans)
