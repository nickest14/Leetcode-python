# 2914. Minimum Number of Changes to Make Binary String Beautiful

class Solution:
    def minChanges(self, s: str) -> int:
        ans: int = 0
        i: int = 0

        while i < len(s):
            if s[i] != s[i + 1]:
                ans += 1
            i += 2

        return ans


ans = Solution().minChanges('1001')
print(ans)
