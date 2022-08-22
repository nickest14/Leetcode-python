# 1408. String Matching in an Array

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for sub_word in words:
            for word in words:
                if sub_word != word and sub_word in word:
                    ans.add(sub_word)
                    break
        return ans

ans = Solution().stringMatching(["mass","as","hero","superhero"])
print(ans)
