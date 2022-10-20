# 1848. Minimum Distance to the Target Element


from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        left = right = start
        while left >= 0 or right < len(nums):
            if left >= 0 and nums[left] == target:
                return start - left
            elif right < len(nums) and nums[right] == target:
                return right - start
            left -= 1
            right += 1


nums = [1, 2, 3, 4, 5]
ans = Solution().getMinDistance(nums, 5, 3)
print(ans)
