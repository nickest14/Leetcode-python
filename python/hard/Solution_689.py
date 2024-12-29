# 689. Maximum Sum of 3 Non-Overlapping Subarrays

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        self.nums = nums
        cur_sum: int = 0
        for i, n in enumerate(nums):
            cur_sum += n
            self.nums[i] = cur_sum

        self.k: int = k
        self.memo: dict = {}
        _, ans = self.window_sum(0, 0)
        return ans

    def window_sum(self, idx: int, used: int) -> tuple[int]:
        if used == 3 or idx + self.k - 1 >= len(self.nums):
            return (0, [])
        if (idx, used) in self.memo:
            return self.memo[(idx, used)]

        take_curr_sum, take_curr_indices = self.window_sum(idx + self.k, used + 1)
        take_curr_sum += (
            self.nums[idx + self.k - 1]
            if idx == 0
            else self.nums[idx + self.k - 1] - self.nums[idx - 1]
        )

        skip_curr_sum, skip_curr_indices = self.window_sum(idx + 1, used)

        if take_curr_sum >= skip_curr_sum:
            self.memo[(idx, used)] = (take_curr_sum, ([idx] + take_curr_indices))
        else:
            self.memo[(idx, used)] = (skip_curr_sum, skip_curr_indices)
        return self.memo[(idx, used)]


ans = Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
# ans = Solution().maxSumOfThreeSubarrays([1, 2, 3, 4], 1)
print(ans)
