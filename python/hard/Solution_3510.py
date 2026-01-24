# 3510. Minimum Pair Removal to Sort Array II

from typing import List
from heapq import heappush, heappop


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n: int = len(nums)
        if n <= 1:
            return 0

        arr: List[int] = [int(x) for x in nums]
        removed: List[bool] = [False] * n
        heap: List[tuple[int, int]] = []
        asc: int = 0
        for i in range(1, n):
            heappush(heap, (arr[i - 1] + arr[i], i - 1))
            if arr[i] >= arr[i - 1]:
                asc += 1
        if asc == n - 1:
            return 0

        rememing: int = n
        prev: List[int] = [i - 1 for i in range(n)]
        nxt: List[int] = [i + 1 for i in range(n)]

        while rememing > 1:
            if not heap:
                break
            sumv, left = heappop(heap)
            right = nxt[left]
            if (
                right >= n
                or removed[left]
                or removed[right]
                or arr[left] + arr[right] != sumv
            ):
                continue

            pre = prev[left]
            after = nxt[right]

            if arr[left] <= arr[right]:
                asc -= 1
            if pre != -1 and arr[pre] <= arr[left]:
                asc -= 1
            if after != n and arr[right] <= arr[after]:
                asc -= 1

            arr[left] += arr[right]
            removed[right] = True
            rememing -= 1

            if pre != -1:
                heappush(heap, (arr[pre] + arr[left], pre))
                if arr[pre] <= arr[left]:
                    asc += 1
            else:
                prev[left] = -1

            if after != n:
                prev[after] = left
                nxt[left] = after
                heappush(heap, (arr[left] + arr[after], left))
                if arr[left] <= arr[after]:
                    asc += 1
            else:
                nxt[left] = n

            if asc == rememing - 1:
                return n - rememing

        return n


ans = Solution().minimumPairRemoval([5, 2, 3, 1])
print(ans)
