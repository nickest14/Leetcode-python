
def linear_search(nums: list, target: int):
    for ind, value in enumerate(nums):
        if value == target:
            return ind
    return None


nums = [1, 5, 10, 2, 20, 3, 8]
ans = linear_search(nums, 20)
print(ans)
