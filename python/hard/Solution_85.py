# 45. Jump Game II

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        cols: int = len(matrix[0])
        heights: list[int] = [0] * cols
        ans: int = 0

        def largestRectangleArea(heights: list[int]) -> int:
            stack: list[int] = []
            max_area: int = 0
            heights.append(0)

            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

            heights.pop()
            return max_area

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            ans = max(ans, largestRectangleArea(heights))

        return ans


ans = Solution().maximalRectangle(
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
)
print(ans)
