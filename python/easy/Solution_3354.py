# 3354. Make Array Elements Equal to Zero

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(i: int, direction: int) -> bool:
            arr: List[int] = nums[:]
            while 0 <= i < len(arr):
                if arr[i] == 0:
                    i += direction
                else:
                    arr[i] -= 1
                    direction *= -1
                    i += direction
            return all(x == 0 for x in arr)

        ans: int = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if simulate(i, 1):
                    ans += 1
                if simulate(i, -1):
                    ans += 1
        return ans


ans = Solution().countValidSelections([1, 0, 2, 0, 3])
print(ans)
