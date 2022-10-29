# 941. Valid Mountain Array

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        left, right = 0, length - 1
        while left < length - 1 and arr[left] < arr[left + 1]:
            left += 1
        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1
        return 0 < left == right < length - 1


ans = Solution().validMountainArray([0, 1, 2, 5,5, 4, 2, 1])
print(ans)
