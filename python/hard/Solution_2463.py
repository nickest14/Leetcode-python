# 2463. Minimum Total Distance Traveled

from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])

        memo: dict[tuple[int], int] = {}

        def helper(curr_robot, curr_fact, used_capacity) -> int:
            if curr_robot == len(robot):
                return 0
            if curr_fact == len(factory):
                return float('inf')

            key: tuple[int] = (curr_robot, curr_fact, used_capacity)
            if key in memo:
                return memo[key]

            min_dist = helper(curr_robot, curr_fact + 1, 0)

            # Option 2: Use current factory if capacity allows
            position, capacity = factory[curr_fact]
            if used_capacity < capacity:
                dist = abs(robot[curr_robot] - position)
                min_dist = min(min_dist, dist + helper(curr_robot + 1, curr_fact, used_capacity + 1))

            memo[key] = min_dist
            return min_dist

        return helper(0, 0, 0)


ans = Solution().minimumTotalDistance([0, 4, 6], [[2, 2], [6, 2]])
# ans = Solution().minimumTotalDistance([0, 4, 6], [[2, 5], [6, 0]])
print(ans)
