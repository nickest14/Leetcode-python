# 944. Delete Columns to Make Sorted

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def generator():
            left, right = 0, len(nums) - 1
            while left < right:
                left_val = nums[left] ** 2
                right_val = nums[right] ** 2
                if left_val > right_val:
                    yield left_val
                    left += 1
                else:
                    yield right_val
                    right -= 1
            yield nums[left] ** 2
        return list(generator())[::-1]


ans = Solution().sortedSquares([-4, -1, 0, 3, 10])
print(ans)
