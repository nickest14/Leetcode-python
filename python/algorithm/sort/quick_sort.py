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


nums = [1, 5, 10, 2, 20, 3, 8]
ans = quick_sort(nums, 0, len(nums) - 1)
print(ans)
