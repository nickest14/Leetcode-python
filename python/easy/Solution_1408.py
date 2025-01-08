# 1408. String Matching in an Array

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans: List[str] = []
        n: int = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans


ans = Solution().stringMatching(["mass", "as", "hero", "superhero"])
print(ans)
