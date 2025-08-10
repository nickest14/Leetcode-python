# 869. Reordered Power of 2


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = sorted(str(n))
        return any(s == sorted(str(1 << i)) for i in range(31))


ans = Solution().reorderedPowerOf2(128)
print(ans)
