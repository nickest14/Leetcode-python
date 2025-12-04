# 2211. Count Collisions on a Road


class Solution:
    def countCollisions(self, directions: str) -> int:
        length: int = len(directions)
        i: int = 0
        j: int = length - 1
        while i < length and directions[i] == "L":
            i += 1

        while j >= 0 and directions[j] == "R":
            j -= 1

        return sum(directions[k] != "S" for k in range(i, j + 1))


ans = Solution().countCollisions("RLRSLL")
print(ans)
