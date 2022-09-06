# 696. Count Binary Substrings


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, pre, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(pre, cur)
                pre, cur = cur, 0
            cur += 1
        return ans + min(pre, cur)


ans = Solution().countBinarySubstrings('1110001')
print(ans)
