# 1299. Replace Elements with Greatest Element on Right Side

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr


ans = Solution().replaceElements([17, 18, 5, 4, 6, 1])
print(ans)
