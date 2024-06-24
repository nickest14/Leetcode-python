# 995. Minimum Number of K Consecutive Bit Flips

from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n, flipped, ans = len(nums), 0, 0
        fp = [0] * n
        for i in range(n):
            if i >= k:
                flipped ^= fp[i - k]
            if flipped == nums[i]:
                if i + k > n:
                    return -1
                fp[i] = 1
                flipped ^= 1
                ans += 1

        return ans


# ans = Solution().minKBitFlips([1, 0, 0, 0, 1, 0, 1, 1, 0], 3)
ans = Solution().minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3)
# ans = Solution().minKBitFlips([0, 1, 0], 1)
print(ans)
