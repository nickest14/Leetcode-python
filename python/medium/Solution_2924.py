# 2924. Find Champion II

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        undeated: list[bool] = [True] * n
        for _, weaker in edges:
            undeated[weaker] = False

        ans: int = -1
        count: int = 0
        for team, win in enumerate(undeated):
            if win:
                ans = team
                count += 1
                if count > 1:
                    return -1

        return ans


ans = Solution().findChampion(3, [[0, 1], [1, 2]])
# ans = Solution().findChampion(4, [[0, 2], [1, 3], [1, 2]])
print(ans)
