# 3637. Trionic Array I

from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        def is_decreasing(a: int, b: int) -> bool:
            if a == 0 or b == len(nums) - 1:
                return False
            for i in range(a, b):
                if nums[i] <= nums[i + 1]:
                    return False
            return True

        n: int = len(nums)
        peak: int = n - 1
        valley: int = 0

        for i in range(n - 1):
            if peak == n - 1 and nums[i] >= nums[i + 1]:
                peak = i
            if valley == 0 and nums[-1 - i] <= nums[-2 - i]:
                valley = n - 1 - i
            if peak < valley:
                return is_decreasing(peak, valley)

        return False


ans = Solution().isTrionic([1, 3, 5, 4, 2, 6])
print(ans)
