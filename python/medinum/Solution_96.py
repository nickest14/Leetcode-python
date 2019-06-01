# 96. Unique Binary Search Trees


class Solution:
    def numTrees(self, n: int) -> int:
        f = [0 for _ in range(n+1)]
        # For initialize f(0) and f(1)
        f[0], f[1] = 1, 1
        if n <= 1:
            return 1
        for k in range(2, n+1):
            for i in range(k):
                f[k] += f[i] * f[k-i-1]
        return f[n]


ans = Solution().numTrees(4)
print(ans)
