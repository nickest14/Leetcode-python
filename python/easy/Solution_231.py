# 231. Power of Two


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


ans = Solution().isPowerOfTwo(32)
print(ans)
