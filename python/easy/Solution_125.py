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


ans = Solution().isPalindrome('A man, a plan, a canal: Panama')
print(ans)
