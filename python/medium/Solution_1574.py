# 1574. Shortest Subarray to be Removed to Make Array Sorted

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n: int = len(arr)

        left: int = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        right: int = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans: int = min(n - left - 1, right)

        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans


# ans = Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5])
ans = Solution().findLengthOfShortestSubarray([1, 2, 3, 6, 5, 10, 17, 18, 13, 20])
print(ans)
