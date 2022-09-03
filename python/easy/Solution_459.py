# 459. Repeated Substring Pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        sub_string = 0
        matching = [0] * length
        for i in range(1, length):
            while sub_string > 0 and s[sub_string] != s[i]:
                sub_string = matching[sub_string-1]
            sub_string += s[sub_string] == s[i]
            matching[i] = sub_string
        return sub_string > 0 and s.startswith(s[sub_string:])

# KMP
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         return s in (2 * s)[1:-1]


# ans = Solution().repeatedSubstringPattern('abcabcabc')
# ans = Solution().repeatedSubstringPattern('abaaabaaaaab')
ans = Solution().repeatedSubstringPattern('abacabacababac')
print(ans)
