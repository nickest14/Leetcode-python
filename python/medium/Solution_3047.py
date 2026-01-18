# 3047. Find the Largest Area of Square Inside Two Rectangles


from typing import List


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        n: int = len(bottomLeft)
        max_side_length: int = 0

        for i in range(n - 1):
            left1, bottom1 = bottomLeft[i]
            right1, top1 = topRight[i]

            for j in range(i + 1, n):
                left2, bottom2 = bottomLeft[j]
                right2, top2 = topRight[j]

                width = min(right1, right2) - max(left1, left2)
                height = min(top1, top2) - max(bottom1, bottom2)

                if width > 0 and height > 0:
                    side_length = min(width, height)
                    max_side_length = max(max_side_length, side_length)

        return max_side_length * max_side_length


ans = Solution().largestSquareArea([[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]])
print(ans)
