# 1356. Sort Integers by The Number of 1 Bits


from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(x: int) -> int:
            cnt: int = 0
            while x:
                x &= x - 1
                cnt += 1
            return cnt

        return sorted(arr, key=lambda x: (countBits(x), x))


ans = Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(ans)
