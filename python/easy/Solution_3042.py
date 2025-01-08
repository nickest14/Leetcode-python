# 3042. Count Prefix and Suffix Pairs I

from typing import List


class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans: int = 0
        n: int = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans


# ans = Solution().countPrefixSuffixPairs(["a","aba","ababa","aa"])
ans = Solution().countPrefixSuffixPairs(["bc","b","ab"])
print(ans)
