# 1922. Count Good Numbers

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD: int = 10 ** 9 + 7
        even_count: int = (n + 1) // 2
        odd_count: int = n // 2
        even_result: int = pow(5, even_count, MOD)
        odd_result: int = pow(4, odd_count, MOD)

        return (even_result * odd_result) % MOD


ans = Solution().countGoodNumbers(4)
print(ans)
