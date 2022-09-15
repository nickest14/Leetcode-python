# 290. Word Pattern

import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        return len(pattern) == len(s) and \
            len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))


ans = Solution().wordPattern('abcd', 'dcba')
print(ans)
