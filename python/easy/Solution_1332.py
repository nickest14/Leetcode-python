# 1332. Remove Palindromic Subsequences

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        else:
            return 2


ans = Solution().removePalindromeSub('aaabbb')
print(ans)
