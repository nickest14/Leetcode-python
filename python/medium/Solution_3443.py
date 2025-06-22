# 3443. Maximum Manhattan Distance After K Changes

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans: int = 0
        north: int = 0
        south: int = 0
        east: int = 0
        west: int = 0

        for i, c in enumerate(s):
            if c == "N":
                north += 1
            elif c == "S":
                south += 1
            elif c == "E":
                east += 1
            elif c == "W":
                west += 1

            current_distance: int = abs(north - south) + abs(east - west)
            total_distance: int = current_distance + min(
                k * 2, i + 1 - current_distance
            )
            ans = max(ans, total_distance)

        return ans


ans = Solution().maxDistance("NWSE", 1)
print(ans)
