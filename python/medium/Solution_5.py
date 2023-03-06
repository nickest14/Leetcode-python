# 5. Longest Palindromic Substring


class Solution:
    def check(self, left: str, right: str):
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            if (right - left + 1) > self.length:
                self.result = self.s[left: right + 1]
                self.length = right - left + 1
            left -= 1
            right += 1

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.result = ''
        self.length = 0

        for i in range(len(s)):
            # odd length
            self.check(i, i)

            # even length
            self.check(i, i + 1)
        return self.result


ans = Solution().longestPalindrome('babad')
print(ans)
