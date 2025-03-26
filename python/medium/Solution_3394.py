# 3394. Check if Grid can be Cut into Sections

from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_cut(axis: int) -> bool:
            rectangles.sort(key=lambda x: x[axis])
            cuts, previous_end = 0, -1
            for rect in rectangles:
                start, end = rect[axis], rect[axis + 2]

                if start >= previous_end:
                    cuts += 1
                previous_end = max(previous_end, end)
                if cuts >= 3:
                    return True

            return False

        return can_cut(0) or can_cut(1)


ans = Solution().checkValidCuts(
    5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
)
print(ans)
