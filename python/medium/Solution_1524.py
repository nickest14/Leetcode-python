# 1524. Number of Sub-arrays With Odd Sum

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod: int = 10**9 + 7
        odd_count, even_count = 0, 1
        prefix_sum, ans = 0, 0

        for a in arr:
            prefix_sum += a
            if prefix_sum % 2 == 1:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1

        return ans % mod


ans = Solution().numOfSubarrays([1, 3, 5])
# ans = Solution().numOfSubarrays([2,4,1,10])
print(ans)
