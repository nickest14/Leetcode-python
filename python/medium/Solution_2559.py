# 2559. Count Vowel Strings in Ranges

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix: list[int] = [0] * (len(words) + 1)
        vowels = {"a", "e", "i", "o", "u"}
        for i, word in enumerate(words):
            prefix[i + 1] = prefix[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] += 1

        ans: list[int] = []
        for q in queries:
            ans.append(prefix[q[1] + 1] - prefix[q[0]])
        return ans


ans = Solution().vowelStrings(
    ["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]
)
print(ans)
