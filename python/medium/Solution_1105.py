# 1105. Filling Bookcase Shelves

from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n: int = len(books)
        f: list[int] = [0] * (n + 1)
        for i, (w, h) in enumerate(books, 1):
            f[i] = f[i - 1] + h
            for j in range(i - 1, 0, -1):
                w += books[j - 1][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j - 1][1])
                f[i] = min(f[i], f[j - 1] + h)

        return f[n]


ans = Solution().minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4)
print(ans)
