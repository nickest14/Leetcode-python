# 3583. Count Special Triplets

from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod: int = 10**9 + 7
        max_val: int = max(nums) * 2
        freq_prev: list[int] = [0] * (max_val + 1)
        freq_next: list[int] = [0] * (max_val + 1)

        for x in nums:
            freq_next[x] += 1

        ans: int = 0
        for x in nums:
            freq_next[x] -= 1
            t = x * 2
            ans = (ans + freq_prev[t] * freq_next[t]) % mod
            freq_prev[x] += 1
        return ans


ans = Solution().specialTriplets([8, 4, 2, 8, 4])
print(ans)
