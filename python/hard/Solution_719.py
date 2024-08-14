# 719. Find K-th Smallest Pair Distance

from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        low, high = 0, nums[-1] - nums[0]

        def count_pairs(max_distance):
            count: int = 0
            right: int = 1
            for left in range(n):
                while right < n and nums[right] - nums[left] <= max_distance:
                    right += 1
                count += right - left - 1
            return count

        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low


# ans = Solution().smallestDistancePair([1, 3, 1], 1)
ans = Solution().smallestDistancePair([1, 2, 4, 6, 9, 20, 30], 4)
print(ans)
