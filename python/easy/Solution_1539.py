# 1539. Kth Missing Positive Number

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid
        return left + k


ans = Solution().findKthPositive([2, 3, 4, 7, 11], 20)
print(ans)
