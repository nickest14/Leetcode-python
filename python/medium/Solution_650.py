# 650. 2 Keys Keyboard


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        ans: int = 0
        factor: int = 2
        while n > 1:
            while n % factor == 0:
                ans += factor
                n //= factor
            factor += 1

        return ans


ans = Solution().minSteps(18)  # 18 = 2 * 3 * 3
ans = Solution().minSteps(10)  # 10 = 2 * 5
print(ans)
