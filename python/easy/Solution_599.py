# 599. Minimum Index Sum of Two Lists

from typing import List
import collections


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_map = {val: ind for ind, val in enumerate(list1)}
        best, ans = float('inf'), []
        for i, val in enumerate(list2):
            if val not in list1_map:
                continue
            if i + list1_map[val] < best:
                best = i + list1_map[val]
                ans = [val]
            elif i + list1_map[val] == best:
                ans.append(val)
        return ans


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
ans = Solution().findRestaurant(list1, list2)
print(ans)
