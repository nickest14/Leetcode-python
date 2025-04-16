# 2179. Count Good Triplets in an Array

from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n: int = len(nums1)
        pos: list[int] = [0] * n
        for i in range(n):
            pos[nums2[i]] = i
        nums1 = [pos[x] for x in nums1]

        bit1: list[int] = [0] * (n + 2)
        bit2: list[int] = [0] * (n + 2)

        def update(bit: list[int], i: int, val: int):
            i += 1
            while i <= n:
                bit[i] += val
                i += i & -i

        def query(bit: list[int], i: int) -> int:
            i += 1
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans: int = 0
        for i in reversed(range(n)):
            x: int = nums1[i]
            val: int = query(bit1, n - 1) - query(bit1, x)
            trip: int = query(bit2, n - 1) - query(bit2, x)
            ans += trip
            update(bit2, x, val)
            update(bit1, x, 1)

        return ans


ans = Solution().goodTriplets([2, 0, 1, 3], [0, 1, 2, 3])
# ans = Solution().goodTriplets([4,0,1,3,2], [4,1,0,2,3])
# ans = Solution().goodTriplets([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
print(ans)
