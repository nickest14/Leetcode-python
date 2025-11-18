# 1437. Check If All 1's Are at Least Length K Places Away

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev: int | None = None
        for i, num in enumerate(nums):
            if num == 1:
                if prev is not None and i - prev <= k:
                    return False
                prev = i
        return True


ans = Solution().kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2)
print(ans)
