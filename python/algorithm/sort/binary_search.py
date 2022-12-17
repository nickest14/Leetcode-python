
def binary_search(nums: list, target: int):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None


nums = [1, 2, 5, 8, 10, 20]
ans = binary_search(nums, 20)
print(ans)
