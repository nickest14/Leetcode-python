
def insertion_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        key = nums[i + 1]
        j = i
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


nums = [1, 5, 10, 2, 20, 3, 8]
ans = insertion_sort(nums)
print(ans)
