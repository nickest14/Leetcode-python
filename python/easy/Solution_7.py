# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x *= -1
            negative = True
        else:
            negative = False
        ans = 0
        while x > 0:
            num = x % 10
            x = int(x / 10)
            ans = ans * 10 + num
        if negative:
            ans *= -1
        if ans > 2**31-1 or ans < -1 * 2**31:
            return 0
        return ans


ans = Solution().reverse(-0)
print(ans)
