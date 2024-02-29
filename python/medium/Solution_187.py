# 187. Repeated DNA Sequences

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        seen = set()
        for i in range(len(s) - 9):
            cur = s[i: i + 10]
            if cur in seen:
                ans.add(cur)
            else:
                seen.add(cur)
        return list(ans)


ans = Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
print(ans)
