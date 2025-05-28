# 2894. Divisible and Non-divisible Sums Difference


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1: int = 0
        num2: int = 0
        for i in range(1, n + 1):
            if i % m != 0:
                num1 += i
            if i % m == 0:
                num2 += i

        return num1 - num2


ans = Solution().differenceOfSums(10, 3)
print(ans)
