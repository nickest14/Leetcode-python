# 14. Longest Common Prefix

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        last = '' if not strs else strs.pop()
        for i, v in enumerate(last):
            for str in strs:
                if i >= len(str) or str[i] != v:
                    return last[:i]
        return last


strs = ["flower", "flow", "flight"]
ans = Solution().longestCommonPrefix(strs)
print(ans)
