# 1400. Construct K Palindrome Strings

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        count_freq = Counter(s)

        odd_count: int = 0
        for c in count_freq:
            if count_freq[c] % 2 == 1:
                odd_count += 1

        return odd_count <= k


ans = Solution().canConstruct("annabelle", 2)
print(ans)
