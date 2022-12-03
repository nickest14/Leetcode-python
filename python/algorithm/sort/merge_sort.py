
def merge(left, right):
    result = []

    while len(left) and len(right):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left if len(left) else result + right


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left_array = nums[:mid]
    right_array = nums[mid:]

    return merge(merge_sort(left_array), merge_sort(right_array))


nums = [1, 5, 10, 2, 20, 3, 8]
ans = merge_sort(nums)
print(ans)
