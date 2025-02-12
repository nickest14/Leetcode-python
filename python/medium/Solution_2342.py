# 2342. Max Sum of a Pair With Equal Sum of Digits

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans: int = -1
        freq: dict[int, int] = {}

        def _digit_sum(num: int) -> int:
            return sum(int(c) for c in str(num))

        for num in nums:
            digit_sum = _digit_sum(num)
            if digit_sum in freq:
                ans = max(ans, freq[digit_sum] + num)
                freq[digit_sum] = max(freq[digit_sum], num)
            else:
                freq[digit_sum] = num

        return ans


ans = Solution().maximumSum([18, 43, 36, 13, 7])
print(ans)
