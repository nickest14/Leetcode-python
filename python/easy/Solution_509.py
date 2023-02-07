# 509. Fibonacci Number


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        pre, cur = 0, 1
        for i in range(1, n):
            pre, cur = cur, pre + cur
        return cur


ans = Solution().fib(6)
print(ans)

[0, 1, 1, 2, 3, 5, 8]
