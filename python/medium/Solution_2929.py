# 2929. Distribute Candies Among Children II


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C2(x: int) -> int:  # Computes C(x,2)
            return (x * (x - 1) // 2) if x >= 2 else 0

        total = (n + 2) * (n + 1) // 2  # C(n+2, 2)
        x1 = n - limit + 1  # Count with a > limit
        t1 = C2(x1)

        x2 = n - 2 * limit  # Count with a & b > limit
        t2 = C2(x2)

        x3 = n - 3 * limit - 1  # Count with a & b & c > limit
        t3 = C2(x3)

        return total - 3 * t1 + 3 * t2 - t3


ans = Solution().distributeCandies(5, 2)
print(ans)
