# 1534. Count Good Triplets

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        - (i < j)
        - (|arr[i] - arr[j]| <= a)
        - (|arr[i] - arr[k]| <= c)
        convert to:       
            arr[i] in ([arr[j] - a, arr[j] + a])
            arr[i] in ([arr[k] - c, arr[k] + c])
        """
        ans: int = 0
        interval: list[int] = [0] * 1001
        for j in range(len(arr)):
            for k in range(j + 1, len(arr)):
                if abs(arr[j] - arr[k]) <= b:
                    left = max(0, max(arr[j] - a, arr[k] - c))
                    right = min(1000, min(arr[j] + a, arr[k] + c))
                    if left <= right:
                        if left == 0:
                            ans += interval[right]
                        else:
                            ans += interval[right] - interval[left - 1]
            for ind in range(arr[j], 1001):
                interval[ind] += 1
        return ans


ans = Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3)
print(ans)
