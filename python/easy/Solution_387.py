# 387. First Unique Character in a String

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for i, v in enumerate(s):
            if counter[v] == 1:
                return i
        return -1


ans = Solution().firstUniqChar('leetcode')
print(ans)
