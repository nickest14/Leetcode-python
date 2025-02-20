# 1415. The k-th Lexicographical String of All Happy Strings of Length n


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(prefix, k: int):
            if len(prefix) == n:
                return prefix
            for c in "abc":
                if prefix and prefix[-1] == c:
                    continue
                cnt = 2 ** (n - len(prefix) - 1)
                if cnt >= k:
                    return dfs(prefix + c, k)
                else:
                    k -= cnt
            return ""

        return dfs("", k)


ans = Solution().getHappyString(3, 5)
print(ans)
