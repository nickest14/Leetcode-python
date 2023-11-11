# 215. Kth Largest Element in an Array

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


class Solution2:
    # Quick sort
    def partition(self, nums: List[int], left: int, right: int):
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot_ind = self.partition(nums, left, right)

            if pivot_ind < kth:
                left = pivot_ind + 1
            elif pivot_ind > kth:
                right = pivot_ind - 1
            else:
                break
        return nums[kth]


ans = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(ans)
