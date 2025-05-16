# 2901. Longest Unequal Adjacent Groups Subsequence II

from typing import List
from functools import lru_cache


class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:

        n: int = len(words)

        @lru_cache(maxsize=n)
        def dp(i: int) -> list[str]:
            longest_chain: list[str] = []
            
            for j in range(i+1, n):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and sum(a != b for a, b in zip(words[i], words[j])) == 1:
                    longest_chain = max(longest_chain, dp(j), key = len)
            
            return [words[i]] + longest_chain
        
        return max([dp(i) for i in range(n)], key = len)


ans = Solution().getWordsInLongestSubsequence(["bab", "dab", "cab"], [1, 2, 2])
print(ans)
