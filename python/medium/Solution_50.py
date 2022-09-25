# 50. Pow(x, n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half_n = int(n/2)
        if n < 0:
            half_n *= -1
            x = 1/x
        val = pow(x, half_n)
        if n % 2 == 0:
            return float(pow(val, 2))
        else:
            return float(pow(val, 2) * x)


# ans = Solution().myPow(34.00515, -3)
ans = Solution().myPow(2, -3)
print(ans)
