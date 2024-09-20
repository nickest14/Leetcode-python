# 214. Shortest Palindrome


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i, n = 0, len(s)
        for c in s[::-1]:
            if c == s[i]:
                i += 1

        if i == n:
            return s
        sub = s[i:]
        return sub[::-1] + self.shortestPalindrome(s[0:i]) + sub


ans = Solution().shortestPalindrome('abcda')
# ans = Solution().shortestPalindrome('abcd')
# ans = Solution().shortestPalindrome('aabb')
# ans = Solution().shortestPalindrome('aacecaaa')
print(ans)
