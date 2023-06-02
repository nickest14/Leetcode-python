# 263. Ugly Number


class Solution:
    def isUgly(self, n: int) -> bool:
        for i in (2, 3, 5):
            while n % i == 0:
                n //= i
        return n == 1


ans = Solution().isUgly(30)
print(ans)
