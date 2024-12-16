# 3264. Final Array State After K Multiplication Operations I

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def get_min_index() -> int:
            min_val: int = float('inf')
            min_ind: int = -1
            for i, num in enumerate(nums):
                if num < min_val:
                    min_val = num
                    min_ind = i
            return min_ind

        while k > 0:
            index = get_min_index()
            nums[index] *= multiplier
            k -= 1
        return nums


ans = Solution().getFinalState([2, 1, 3, 5, 6], 5, 2)
print(ans)
