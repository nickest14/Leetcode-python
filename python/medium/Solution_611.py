# 611. Valid Triangle Number
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n: list[int] = len(nums)
        ans: int = 0

        for i in range(n - 1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans


ans = Solution().triangleNumber([2, 2, 3, 4])
print(ans)
