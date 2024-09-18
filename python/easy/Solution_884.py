# 884. Uncommon Words from Two Sentences

from typing import List
from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words: list[str] = s1.split() + s2.split()
        dic: dict[str, int] = defaultdict(int)
        for word in words:
            dic[word] += 1

        return [word for word, count in dic.items() if count == 1]


s1 = 'this apple is sweet'
s2 = 'this apple is sour'
ans = Solution().uncommonFromSentences(s1, s2)
print(ans)
