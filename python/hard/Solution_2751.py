# 2751. Robot Collisions

from typing import List


class Robot():
    def __init__(self, position: int, health: int, direction: str, index: int):
        self.position = position
        self.health = health
        self.direction = direction
        self.index = index


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n: int = len(positions)
        robots: List[Robot] = [Robot(positions[i], healths[i], directions[i], i) for i in range(n)]
        robots.sort(key=lambda x: x.position)

        stack: List[Robot] = []
        for robot in robots:
            if robot.direction == 'R':
                stack.append(robot)
                continue
            gone = False
            while stack and stack[-1].health <= robot.health and stack[-1].direction == 'R':
                if stack[-1].health == robot.health:
                    stack.pop()
                    gone = True
                    break
                robot.health -= 1
                stack.pop()

            if not gone and stack and stack[-1].direction == 'R' and stack[-1].health > robot.health:
                stack[-1].health -= 1
                gone = True

            if not gone:
                stack.append(robot)

        stack.sort(key=lambda x: x.index)
        return [robot.health for robot in stack]


positions = [3, 5, 2, 6]
healths = [10, 10, 15, 12]
directions = "RLRL"
ans = Solution().survivedRobotsHealths(positions, healths, directions)
print(ans)
