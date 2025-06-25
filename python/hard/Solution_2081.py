# 2081. Sum of k-Mirror Numbers


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def createPalindrome(num: int, odd: bool) -> int:
            x: int = num
            if odd:
                x //= 10
            while x > 0:
                num = num * 10 + x % 10
                x //= 10
            return num

        def isPalindrome(num: int) -> bool:
            digits: list[int] = []
            while num > 0:
                digits.append(num % k)
                num //= k
            return digits == digits[::-1]

        ans: int = 0
        length: int = 1
        while n > 0:
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p: int = createPalindrome(i, True)
                if isPalindrome(p):
                    ans += p
                    n -= 1
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p: int = createPalindrome(i, False)
                if isPalindrome(p):
                    ans += p
                    n -= 1
            length *= 10
        return ans


ans = Solution().kMirror(2, 15)
print(ans)
