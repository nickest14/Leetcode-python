# 2942. Find Words Containing Character

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]



ans = Solution().findWordsContaining(["leet","code"], 'e')
print(ans)
