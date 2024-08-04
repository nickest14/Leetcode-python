# 1508. Range Sum of Sorted Subarray Sums

from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums: list[int] = []
        for i in range(n):
            current_sum: int = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)

        subarray_sums.sort()
        return sum(subarray_sums[left - 1: right]) % (10**9 + 7)


ans = Solution().rangeSum([1, 2, 3, 4], 4, 1, 5)
print(ans)
