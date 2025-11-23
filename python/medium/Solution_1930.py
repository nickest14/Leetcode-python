# 1930. Unique Length-3 Palindromic Subsequences

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans: int = 0
        uniq: set[str] = set(s)
        for c in uniq:
            start, end = s.find(c), s.rfind(c)
            if start < end:
                ans += len(set(s[start + 1: end]))
        return ans


ans = Solution().countPalindromicSubsequence('ababcab')
print(ans)
