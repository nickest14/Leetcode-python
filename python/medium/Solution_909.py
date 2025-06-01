# 909. Snakes and Ladders

from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length: int = len(board)

        def int_to_pos(square: int) -> list[int]:
            r = length - 1 - ((square - 1) // length)
            c = (square - 1) % length
            if (length % 2 == 0 and r % 2 == 0) or (length % 2 != 0 and r % 2 != 0):
                c = length - 1 - c
            return [r, c]

        q: deque[tuple[int, int]] = deque()  # (square, moves)
        q.append((1, 0))
        visit: set[int] = set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = int_to_pos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == length * length:
                    return moves + 1
                if next_square not in visit:
                    visit.add(next_square)
                    q.append((next_square, moves + 1))
        return -1


board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], 
         [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
# board = [[-1, -1, 19, 10, -1], [2, -1, -1, 6, -1], [-1, 17, -1, 19, -1], [25, -1, 20, -1, -1], [-1, -1, -1, -1, 15]]
ans = Solution().snakesAndLadders(board)
print(ans)
