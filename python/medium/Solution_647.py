# 647. Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        self.s = s
        self.length = len(s)
        ans = 0
        for i in range(self.length):
            ans += self.count_palindromic(i, i)
            ans += self.count_palindromic(i, i + 1)

        return ans

    def count_palindromic(self, left: int, right: int):
        count = 0
        while left >= 0 and right < self.length and self.s[left] == self.s[right]:
            count += 1
            left -= 1
            right += 1
        return count


ans = Solution().countSubstrings('abc')
print(ans)
