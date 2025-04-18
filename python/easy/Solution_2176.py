# 2176. Count Equal and Divisible Pairs in an Array

from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_to_indices = defaultdict(list)
        ans: int = 0

        for curr_idx, curr_num in enumerate(nums):
            for prev_idx in num_to_indices[curr_num]:
                if (curr_idx * prev_idx) % k == 0:
                    ans += 1
            num_to_indices[curr_num].append(curr_idx)

        return ans


ans = Solution().countPairs([3, 1, 2, 2, 2, 1, 3], 2)
print(ans)
