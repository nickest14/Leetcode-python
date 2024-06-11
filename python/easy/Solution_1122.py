# 1122. Relative Sort Array

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index_map = {num: idx for idx, num in enumerate(arr2)}

        def custom_sort(num):
            return index_map.get(num, len(arr2) + num)

        arr1.sort(key=custom_sort)
        return arr1


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
ans = Solution().relativeSortArray(arr1, arr2)
print(ans)
