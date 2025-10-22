# 3346. Maximum Frequency of an Element After Performing Operations I

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        max_num: int = max(nums)
        n: int = max_num + k + 2
        freq: list[int] = [0] * n
        for num in nums:
            freq[num] += 1

        pre: list[int] = [0] * n
        pre[0] = freq[0]
        for idx in range(1, n):
            pre[idx] = pre[idx - 1] + freq[idx]

        ans: int = 0
        for idx in range(n):
            if freq[idx] == 0 and numOperations == 0:
                continue
            left, right = max(0, idx - k), min(n - 1, idx + k)
            total: int = pre[right] - (pre[left - 1] if left > 0 else 0)
            adjacent: int = total - freq[idx]
            value: int = freq[idx] + min(numOperations, adjacent)
            ans = max(ans, value)
        return ans


# ans = Solution().maxFrequency([1, 4, 5], 1, 2)
ans = Solution().maxFrequency([88, 53], 27, 2)
print(ans)
