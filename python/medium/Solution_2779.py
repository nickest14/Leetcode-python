# 2779. Maximum Beauty of an Array After Applying Operation

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left: int = 0
        ans: int = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)

        return ans


# class Solution:
#     def maximumBeauty(self, nums: List[int], k: int) -> int:
#         events: list[tuple[int]] = []
#         for num in nums:
#             events.append((num - k, 1))
#             events.append((num + k + 1, -1))
#         events.sort()

#         ans: int = 0
#         current_count: int = 0
#         for _, effect in events:
#             current_count += effect
#             ans = max(ans, current_count)

#         return ans


ans = Solution().maximumBeauty([4, 6, 1, 2], 2)
# ans = Solution().maximumBeauty([1, 10], 2)
print(ans)
