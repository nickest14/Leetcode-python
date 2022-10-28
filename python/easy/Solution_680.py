# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(start: int, end: int) -> bool:
            sub_str = s[start:end + 1]
            return sub_str == sub_str[::-1]

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True


ans = Solution().validPalindrome('abca')
# ans = Solution().validPalindrome('deeee')
# ans = Solution().validPalindrome('eccer')
print(ans)
