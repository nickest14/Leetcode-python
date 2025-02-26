# 873. Length of Longest Fibonacci Subsequence


from typing import List
from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        lookup: dict[dict[int, int]] = {}
        max_length: int = 0

        for cur_index, cur_val in enumerate(arr):
            lookup[cur_val] = defaultdict(lambda: 2)  # Default sequence length is 2
            for prev_index in range(cur_index - 1, -1, -1):
                prev_val = arr[prev_index]
                prev2_val = cur_val - prev_val
                if prev2_val >= prev_val:
                    break

                if prev2_val in lookup:
                    lookup[cur_val][prev_val] = (
                        lookup[prev_val][prev2_val] + 1
                    )
                    max_length = max(max_length, lookup[cur_val][prev_val])

        return max_length


ans = Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8])
print(ans)
