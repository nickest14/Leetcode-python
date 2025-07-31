# 2411. Smallest Subarrays With Maximum Bitwise OR

from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        ans: list[int] = [0] * n

        latest: list[int] = [-1] * 32

        for i in range(n - 1, -1, -1):
            farthest: int = i
            for b in range(32):
                if (nums[i] >> b) & 1:
                    latest[b] = i
                if latest[b] != -1:
                    farthest = max(farthest, latest[b])
            ans[i] = farthest - i + 1

        return ans


ans = Solution().smallestSubarrays([1, 0, 2, 1, 3])
print(ans)
