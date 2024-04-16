# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        cur_sum = sum(arr[:k - 1])
        for L in range(len(arr) - k + 1):
            cur_sum += arr[L + k - 1]
            if (cur_sum / k) >= threshold:
                ans += 1
            cur_sum -= arr[L]

        return ans


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
ans = Solution().numOfSubarrays(arr, k, threshold)
print(ans)
