# 1684. Count the Number of Consistent Strings

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count: int = 0
        for word in words:
            for c in word:
                if c not in allowed_set:
                    count += 1
                    break

        return len(words) - count

    # # Another solution
    # def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    #     allowed = set(allowed)
    #     ans:int = 0

    #     for word in words:
    #         if set(word) <= allowed:
    #             ans +=1
    #     return ans


ans = Solution().countConsistentStrings('ab', ['ad', 'bd', 'aaab', 'baa', 'badab'])
print(ans)
