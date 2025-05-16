# 2900. Longest Unequal Adjacent Groups Subsequence I

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans: list[str] = [words[0]]
        for i in range(1, len(words)):
            if groups[i] != groups[i - 1]:
                ans.append(words[i])

        return ans


ans = Solution().getLongestSubsequence(["e", "a", "b"], [0, 0, 1])
print(ans)
