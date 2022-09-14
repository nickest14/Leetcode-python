# 242. Valid Anagram

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


ans = Solution().isAnagram('abcd', 'dcba')
print(ans)
