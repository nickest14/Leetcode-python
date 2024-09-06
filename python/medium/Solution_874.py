# 874. Walking Robot Simulation

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, dir = 0, 0, 0
        direction: list[tuple[int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacle_set: set[tuple[int]] = set(map(tuple, obstacles))

        ans: int = 0
        for cmd in commands:
            if cmd == -1:
                dir = (dir + 1) % 4
            elif cmd == -2:
                dir = (dir - 1) % 4
            else:
                for _ in range(cmd):
                    nx, ny = x + direction[dir][0], y + direction[dir][1]
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)

        return ans


commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
ans = Solution().robotSim(commands, obstacles)
print(ans)
