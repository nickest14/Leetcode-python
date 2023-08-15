# 300. Longest Increasing Subsequence

from typing import List


class Solution:
    # DP
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)

    # DP with binary search
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = []

    #     for num in nums:
    #         left, right = 0, len(dp)
    #         while left < right:
    #             mid = left + (right - left) // 2
    #             if dp[mid] < num:
    #                 left = mid + 1
    #             else:
    #                 right = mid
    #         if right == len(dp):
    #             dp.append(num)
    #         else:
    #             dp[right] = num

    #     return len(dp)


ans = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(ans)
