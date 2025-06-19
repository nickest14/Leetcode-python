# 2294. Partition Array Such That Maximum Difference Is K

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans: int = 1
        min_num: int = nums[0]
        for num in nums[1:]:
            if num - min_num > k:
                ans += 1
                min_num = num
        return ans

ans = Solution().partitionArray([3,6,1,2,5], 2)
print(ans)
