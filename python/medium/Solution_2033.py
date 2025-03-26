# 2033. Minimum Operations to Make a Uni-Value Grid

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rem: int = grid[0][0] % x
        arr: list[int] = []

        for row in grid:
            for num in row:
                if num % x != rem:
                    return -1
                arr.append(num)

        arr.sort()
        mid: int = arr[len(arr) // 2]
        return sum(abs(num - mid) // x for num in arr)


# ans = Solution().minOperations([[2, 4], [6, 8]], 2)
# ans = Solution().minOperations([[2, 4], [10, 8]], 2)
ans = Solution().minOperations([[3, 5], [11, 9]], 2)
print(ans)
