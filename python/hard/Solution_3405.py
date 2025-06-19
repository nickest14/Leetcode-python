# 3405. Count the Number of Arrays with K Matching Adjacent Elements

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7

        def modinv(x):
            return pow(x, mod - 2, mod)
        
        max_n = n
        fact = [1] * (max_n)
        for i in range(1, max_n):
            fact[i] = (fact[i - 1] * i) % mod
        
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return (fact[a] * modinv(fact[b]) % mod) * modinv(fact[a - b]) % mod

        comb_part = comb(n - 1, k)
        power_part = pow(m - 1, n - 1 - k, mod)

        return comb_part * m % mod * power_part % mod


ans = Solution().countGoodArrays(3, 2, 1)
print(ans)
