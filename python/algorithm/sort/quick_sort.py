from typing import List


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort(nums: List, low: int, high: int) -> List:
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)

    return nums

# # recursive version, not good
# def quick_sort(nums):
#     n = len(nums)
#     if n <= 1:
#         return nums
#     left = []
#     right = []
#     pivot = nums[0]
#     for i in range(1,n):
#         if nums[i] < pivot:
#             left.append(nums[i])
#         else:
#             right.append(nums[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)

nums = [1, 5, 10, 2, 20, 3, 8]
ans = quick_sort(nums, 0, len(nums) - 1)
print(ans)
