# 912. Sort an Array


from typing import List


# Merge sort
class Solution:
    def merge(self, left, right):
        result = []

        while len(left) and len(right):
            if (left[0] < right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        return result + left if len(left) else result + right

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        left_array = nums[:mid]
        right_array = nums[mid:]

        return self.merge(self.sortArray(left_array), self.sortArray(right_array))


# Quick sort
class Solution2:
    def partitoin(self, nums: list, low: int, high: int):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quick_sort(self, nums: list, left: int, right: int):
        if left < right:
            pi = self.partitoin(nums, left, right)
            self.quick_sort(nums, left, pi - 1)
            self.quick_sort(nums, pi + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums


# ans = Solution().sortArray([5, 2, 3, 1])
ans = Solution().sortArray([9, 10, 1, 3, 4, 2])
print(ans)
