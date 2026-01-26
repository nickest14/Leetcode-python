# 1200. Minimum Absolute Difference


from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans: List[List[int]] = []
        min_diff: int = float("inf")
        for i in range(1, len(arr)):
            diff: int = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                ans = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                ans.append([arr[i - 1], arr[i]])

        return ans


ans = Solution().minimumAbsDifference([4, 2, 1, 3])
print(ans)
