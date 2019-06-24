# 9. Palindrome Number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


ans = Solution().isPalindrome(4)
print(ans)
