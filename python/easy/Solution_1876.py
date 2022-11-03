# 1876. Substrings of Size Three with Distinct Characters

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: 
            return 0
        return sum(s[i] != s[i - 1] != s[i - 2] != s[i] for i in range(2, len(s)))


ans = Solution().countGoodSubstrings('xyzzaz')
print(ans)
