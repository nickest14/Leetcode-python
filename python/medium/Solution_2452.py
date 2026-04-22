# 2452. Words Within Two Edits of Dictionary

from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def _get_distance(s1: str, s2: str):
            cnt: int = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
                if cnt > 2:
                    return False
            return True

        ans: list[str] = []
        for query in queries:
            for d in dictionary:
                if _get_distance(query, d):
                    ans.append(query)
                    break
        return ans


ans = Solution().twoEditWords(
    ["word", "note", "ants", "wood"], ["wood", "joke", "moat"]
)
# ans = Solution().partitionString("ssssss")
print(ans)
