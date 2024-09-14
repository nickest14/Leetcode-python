# 2419. Longest Subarray With Maximum Bitwise AND

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans: int = 0
        cur_len: int = 0
        max_num: int = max(nums)
        for num in nums:
            if num == max_num:
                cur_len += 1
            else:
                ans = max(ans, cur_len)
                cur_len = 0
        return max(ans, cur_len)


ans = Solution().longestSubarray([1, 2, 3, 3, 2, 2])
print(ans)
