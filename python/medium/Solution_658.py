# 658. Find K Closest Elements

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        val, idx = arr[0], 0
        while l <= r:
            m = (l + r) // 2
            cur_diff, res_diff = abs(arr[m] - x), abs(val - x)
            if cur_diff < res_diff or (cur_diff == res_diff and arr[m] < val):
                val, idx = arr[m], m
            if arr[m] < x:
                l = m + 1
            elif arr[m] > x:
                r = m - 1
            else:
                break

        l = r = idx
        for _ in range(k - 1):
            if l == 0:
                r += 1
            elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
                l -= 1
            else:
                r += 1

        return arr[l: r + 1]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
ans = Solution().findClosestElements(arr, k, x)
print(ans)
