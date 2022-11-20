# 733. Flood Fill

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i: int, j: int):
            if (0 <= i < col and 0 <= j < row and image[i][j] == old_color):
                image[i][j] = color
                for r, c in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    dfs(r, c)

        # def bfs(i: int, j: int):
        #     import collections
        #     queue = collections.deque([(sr, sc)])
        #     while queue:
        #         r, c = queue.popleft()
        #         image[r][c] = color
        #         for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
        #             if 0 <= i < col and 0 <= j < row and image[i][j] == old_color:
        #                 queue.append((i, j))

        if not any(image) or image[sr][sc] == color:
            return image
        col, row = len(image), len(image[0])
        old_color = image[sr][sc]
        dfs(sr, sc)
        # bfs(sr, sc)
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
ans = Solution().floodFill(image, sr, sc, color)
print(ans)
