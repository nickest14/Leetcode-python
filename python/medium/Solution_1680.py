# 1680. Concatenation of Consecutive Binary Numbers


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod: int = 10**9 + 7
        ans: int = 0
        for i in range(1, n + 1):
            ans = (ans << (len(bin(i)) - 2)) + i
            ans %= mod
        return ans


ans = Solution().concatenatedBinary(3)
print(ans)
