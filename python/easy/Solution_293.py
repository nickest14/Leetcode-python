# 293. Flip Game

from typing import List
import itertools
import operator


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        return [s[:i-1] + '--' + s[i+1:] for i in range(1, len(s)) if s[i-1:i+1] == '++']


ans = Solution().generatePossibleNextMoves('++++')
print(ans)
