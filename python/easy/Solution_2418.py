# 2418. Sort the People

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        return [x[0] for x in mapping]


ans = Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170])
print(ans)
