# 1089. Duplicate Zeros

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n, zeros = len(arr), arr.count(0)
        for i in reversed(range(len(arr))):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0


ans = Solution().duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
print(ans)
