
def radix_sort(nums):
    max_num = max(nums)
    digits = 1
    while max_num >= 10 ** digits:
        digits += 1
    for i in range(digits):
        buckets = [[] for _ in range(10)]
        for num in nums:
            radix = int(num / (10 ** i) % 10)
            buckets[radix].append(num)
        ind = 0
        for bucket_num in range(10):
            for num in buckets[bucket_num]:
                nums[ind] = num
                ind += 1
    return nums


nums = [28, 96, 5, 33, 60, 169, 170, 249, 362, 44, 84, 123]
ans = radix_sort(nums)
print(ans)
