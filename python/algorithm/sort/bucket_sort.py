import math


def bucket_sort(nums):
    max_val, min_val = max(nums), min(nums)
    size = 10

    buckets = [[] for i in range(math.floor((max_val - min_val) / size + 1))]

    for i in range(len(nums)):
        val = nums[i]
        buckets[math.floor((val - min_val) / size)].append(val)

    result = []
    for i in range(len(buckets)):
        buckets[i].sort()
        for j in range(len(buckets[i])):
            result.append(buckets[i][j])
    return result


nums = [1, 5, 10, 2, 20, 3, 8, 200]
ans = bucket_sort(nums)
print(ans)
