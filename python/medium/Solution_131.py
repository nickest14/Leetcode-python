# 131. Palindrome Partitioning


class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def partition(self, s):
        res = []
        self.helper(s, res, [])
        return res

    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], res, path + [s[:i]])


ans = Solution().partition('aabbc')
print(ans)
