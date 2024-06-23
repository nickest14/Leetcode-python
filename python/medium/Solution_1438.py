# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        max_q, min_q = deque(), deque()
        length = len(nums)
        j = 0

        for i in range(length):
            while max_q and nums[i] > max_q[-1]:
                max_q.pop()
            max_q.append(nums[i])

            while min_q and nums[i] < min_q[-1]:
                min_q.pop()
            min_q.append(nums[i])

            if max_q[0] - min_q[0] > limit:
                if nums[j] == max_q[0]:
                    max_q.popleft()
                if nums[j] == min_q[0]:
                    min_q.popleft()
                j += 1
            ans = max(ans, i - j + 1)

        return ans

    # # Timeout solution
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     ans = 0
    #     start, end = 0, len(nums)
    #     right = start

    #     while start < end and right < end:
    #         tmp_nums = [nums[j] for j in range(start, right + 1)]
    #         max_diff = max(tmp_nums) - min(tmp_nums)
    #         if max_diff <= limit:
    #             ans = max(ans, len(tmp_nums))
    #             right += 1
    #         else:
    #             start += 1
    #             right = start

    #     return ans


# ans = Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5)
# ans = Solution().longestSubarray([6, 2, 2, 7, 1, 6], 5)
ans = Solution().longestSubarray([1, 2, 10], 5)
print(ans)

