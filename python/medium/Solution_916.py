# 916. Word Subsets


from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans: list[str] = []
        freq = Counter()
        for word in words2:
            cur = Counter(word)
            for c in cur:
                if freq[c] < cur[c]:
                    freq[c] = cur[c]

        for word in words1:
            cur = Counter(word)
            if all(cur[chr] >= freq[chr] for chr in freq):
                ans.append(word)

        return ans


ans = Solution().wordSubsets(
    ["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]
)
print(ans)
