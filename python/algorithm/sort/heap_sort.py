from typing import List


def heapify(nums, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # if left child of root exists and is greater than root
    if left < n and nums[i] < nums[left]:
        largest = left

    # if right child of root exists and is greater than root
    if right < n and nums[largest] < nums[right]:
        largest = right

    if largest != i:
        (nums[i], nums[largest]) = (nums[largest], nums[i])
        # Heapify the root.
        heapify(nums, n, largest)


def heap_sort(nums: List) -> List:
    n = len(nums)
    # Build a maxheap. Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        (nums[i], nums[0]) = (nums[0], nums[i])
        heapify(nums, i, 0)

    return nums


nums = [1, 5, 10, 2, 20, 3, 8, 9]
ans = heap_sort(nums)
print(ans)
