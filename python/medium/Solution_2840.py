# 2840. Check if Strings Can be Made Equal With Operations II

from collections import Counter

    
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odds_s1 = Counter(s1[1::2])
        evens_s1 = Counter(s1[::2])

        odds_s2 = Counter(s2[1::2])
        evens_s2 = Counter(s2[::2])

        return odds_s1 == odds_s2 and evens_s1 == evens_s2


ans = Solution().checkStrings("abcdba", "cabdab")
print(ans)
