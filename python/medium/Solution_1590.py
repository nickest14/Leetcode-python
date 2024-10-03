# 1590. Make Sum Divisible by P

from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total: int = sum(nums)
        remainder: int = total % p
        if remainder == 0:
            return 0

        def find_smallest_subarray():
            prefix_sum: int = 0
            min_length = len(nums)
            prefix_map = {0: -1}  # Store prefix sums with their index

            for i, num in enumerate(nums):
                prefix_sum += num
                target_remainder = (prefix_sum % p - remainder) % p
                if target_remainder in prefix_map:
                    min_length = min(min_length, i - prefix_map[target_remainder])

                prefix_map[prefix_sum % p] = i

            return min_length

        ans: int = find_smallest_subarray()
        return ans if ans < len(nums) else -1


ans = Solution().minSubarray([3, 1, 4, 2], 6)
# ans = Solution().minSubarray([1, 3, 5, 9, 2], 6)
print(ans)
