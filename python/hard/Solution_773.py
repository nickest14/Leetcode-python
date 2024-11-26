# 773. Sliding Puzzle

from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target: str = '123450'
        start = ''.join(str(num) for row in board for num in row)
        neighbors: dict[int, list[int]] = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        # BFS setup
        queue = deque([(start, 0)])  # (state, moves)
        visited = set()
        visited.add(start)

        while queue:
            state, moves = queue.popleft()

            if state == target:
                return moves

            # Find the index of zero
            zero_index = state.index('0')

            # Generate new states by swapping '0' with its neighbors
            for neighbor in neighbors[zero_index]:
                new_state = list(state)
                # Swap '0' with the neighbor
                new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))

        return -1


ans = Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]])
print(ans)
