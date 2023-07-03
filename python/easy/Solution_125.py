# 125. Valid Palindrome
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s:
            rule = '[a-zA-Z0-9]+'
            s = re.findall(rule, s)
            text = ''
            for i in s:
                text += i
            return text.lower() == text[::-1].lower()
        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")
        )


ans = Solution().isPalindrome('A man, a plan, a canal: Panama')
print(ans)
