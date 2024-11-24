# 1861. Rotating the Box

from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        ans: list[list[int]] = [['.'] * rows for _ in range(cols)]

        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if box[r][c] == '#':
                    ans[i][rows - r - 1] = '#'
                    i -= 1
                elif box[r][c] == '*':
                    ans[c][rows - r - 1] = '*'
                    i = c - 1

        return ans


# ans = Solution().rotateTheBox(
#     [
#         ["#", ".", "*", "."],
#         ["#", "#", "*", "."]
#     ]
# )
ans = Solution().rotateTheBox(
    [
        ["#", "#", "*", ".", "*", "."],
        ["#", "#", "#", "*", ".", "."],
        ["#", "#", "#", ".", "#", "."]
    ]
)
print(ans)
