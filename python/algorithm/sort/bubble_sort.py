from typing import List


def bubble_sort(nums: List) -> List:
    length = len(nums)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


ans = bubble_sort([1, 5, 10, 2, 20, 3, 8])
print(ans)
