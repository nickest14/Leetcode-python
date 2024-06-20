# 424. Longest Repeating Character Replacement


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        count = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans


ans = Solution().characterReplacement("ABAB", 2)
print(ans)
