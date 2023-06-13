# 1837. Sum of Digits in Base K

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n:
            n, r = divmod(n, k)
            ans += r
        return ans


# ans = Solution().sumBase(34, 6)
ans = Solution().sumBase(90, 9)
print(ans)
