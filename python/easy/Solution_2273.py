# 2273. Find Resultant Array After Removing Anagrams

from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n: int = len(words)
        freq: list[Counter] = [Counter(w) for w in words]
        ans: list[str] = [words[0]]
        for i in range(1, n):
            if freq[i] != freq[i - 1]:
                ans.append(words[i])
        return ans


ans = Solution().removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"])
print(ans)
