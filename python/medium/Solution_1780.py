# 1780. Check if Number is a Sum of Powers of Three


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power: int = 1
        while power * 3 <= n:
            power *= 3

        while n > 0 and power > 0:
            if n >= power:
                n -= power
            power //= 3
        return n == 0


ans = Solution().checkPowersOfThree(12)
print(ans)
