# 1513. Number of Substrings With Only 1s


class Solution:
    def numSub(self, s: str) -> int:
        ans: int = 0
        for part in s.split("0"):
            n: int = len(part)
            ans += (n * (n + 1)) // 2
        return ans % (10**9 + 7)


ans = Solution().numSub("0110111")
print(ans)
