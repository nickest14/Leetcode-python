
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


ans = selection_sort([1, 5, 10, 2, 20, 3, 8])
print(ans)
