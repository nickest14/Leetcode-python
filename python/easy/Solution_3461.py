# 3461. Check If Digits Are Equal in String After Operations I


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits: list[int] = [int(c) for c in s]
        n: int = len(digits)
        while n > 2:
            for i in range(n - 1):
                digits[i] = (digits[i] + digits[i + 1]) % 10
            n -= 1
        return digits[0] == digits[1]


ans = Solution().hasSameDigits("3902")
print(ans)
