# 2833. Furthest Point From Origin


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left: int = 0
        right: int = 0
        distance: int = 0
        for move in moves:
            if move == "L":
                left += 1
            elif move == "R":
                right += 1
            else:
                distance += 1

        return abs(left - right) + distance


ans = Solution().furthestDistanceFromOrigin("L_RL__R")
print(ans)
