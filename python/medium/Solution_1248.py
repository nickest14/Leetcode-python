# 1248. Count Number of Nice Subarrays

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        left, right = 0, 0
        odd_count = 0
        cur_sub_count = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
                cur_sub_count = 0

            while odd_count == k:
                cur_sub_count += 1
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            ans += cur_sub_count

        return ans


ans = Solution().numberOfSubarrays([1, 1, 2, 1, 1, 1, 4], 3)
print(ans)
