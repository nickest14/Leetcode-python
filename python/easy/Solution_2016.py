# 2016. Maximum Difference Between Increasing Elements

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num: int = nums[0]
        ans: int = -1

        for num in nums[1:]:
            if num > min_num:
                ans = max(ans, num - min_num)
            else:
                min_num = num

        return ans


ans = Solution().maximumDifference([7, 1, 5, 4])
# ans = Solution().maximumDifference([9, 4, 3, 2])
print(ans)
