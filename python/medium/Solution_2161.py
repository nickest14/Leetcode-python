# 2161. Partition Array According to Given Pivot

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, larger, equal = [], [], []

        for i in range(len(nums)):
            if nums[i] < pivot:
                smaller.append(nums[i])
            elif nums[i] > pivot:
                larger.append(nums[i])
            else:
                equal.append(nums[i])

        return smaller + equal + larger


ans = Solution().pivotArray([9, 12, 5, 10, 14, 3, 10], 10)
print(ans)
