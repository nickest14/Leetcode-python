# 324. Wiggle Sort II

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = (len(nums) - 1) // 2
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

# import random
# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         def find_median() -> int:
#             left, mid, right = 0, len(nums) // 2, len(nums) - 1
#             while True:
#                 pivot = random.randint(left, right)
#                 nums[pivot], nums[right] = nums[right], nums[pivot]
#                 pivot = left
#                 for i in range(left, right):
#                     if nums[i] < nums[right]:
#                         nums[pivot], nums[i] = nums[i], nums[pivot]
#                         pivot += 1
#                 nums[right], nums[pivot] = nums[pivot], nums[right]
#                 if pivot < mid:
#                     left = pivot + 1
#                 elif mid < pivot:
#                     right = pivot - 1
#                 else:
#                     return nums[pivot]

#         mid = find_median()
#         virtual = lambda i: (1 + 2 * i) % (len(nums) | 1)
#         j, k = 0, 0
#         for i in range(len(nums)):
#             vi = virtual(i)
#             if nums[vi] > mid:
#                 vj = virtual(j)
#                 nums[vi], nums[vj] = nums[vj], nums[vi]
#                 j += 1
#                 if k < j:
#                     k += 1
#             if nums[vi] == mid:
#                 vk = virtual(k)
#                 nums[vi], nums[vk] = nums[vk], nums[vi]
#                 k += 1


Solution().wiggleSort([1, 6, 2, 4, 1, 3, 7])
