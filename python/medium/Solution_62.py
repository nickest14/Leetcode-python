# 62. Unique Paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array = [[0 for i in range(n+1)] for j in range(m+1)]
        print(array)

        def getorupdate(m, n):
            if array[m][n] == 0:
                array[m][n] = dfs(m, n)
            return array[m][n]

        def dfs(m, n):
            if m == 1 and n == 1:
                return 1
            elif m < 1 or n < 1:
                return 0
            return getorupdate(m - 1, n) + getorupdate(m, n - 1)
        return dfs(m, n)

    # USe dfs, but time limit exceeded
    def uniquePaths_dfs(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        elif m < 1 or n < 1:
            return 0
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


ans = Solution().uniquePaths(5, 2)
print(ans)
