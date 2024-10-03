# 1331. Rank Transform of an Array

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_mapping: dict[int, int] = {}
        sorted_numbers: list[int] = sorted(list(set(arr)))
        for ind, val in enumerate(sorted_numbers):
            rank_mapping[val] = ind + 1

        for ind, val in enumerate(arr):
            arr[ind] = rank_mapping[val]

        return arr


ans = Solution().arrayRankTransform([40, 10, 20, 30])
print(ans)
