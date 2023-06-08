# 342. Power of Four


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n % 3 == 1 and n & (n - 1) == 0


ans = Solution().isPowerOfFour(-4)
print(ans)
