# 3097. Shortest Subarray With OR at Least K II

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1

        ans: int = len(nums) + 1
        count: list[int] = [0] * 32
        val: int = 0
        start: int = 0

        for i in range(len(nums)):
            num = nums[i]
            val |= num
            ibit = 0
            while num:
                count[ibit] += num & 1
                num >>= 1
                ibit += 1

            while val >= k and start < len(nums):
                ans = min(ans, i - start + 1)
                num = nums[start]
                start += 1
                ibit = 0
                while num:
                    count[ibit] -= num & 1
                    if count[ibit] == 0:
                        val &= ~(1 << ibit)
                    num >>= 1
                    ibit += 1

        return -1 if ans == len(nums) + 1 else ans


ans = Solution().minimumSubarrayLength([2, 1, 8], 10)
# ans = Solution().minimumSubarrayLength([1, 1, 5, 1, 1], 3)
print(ans)
