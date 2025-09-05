# 3516. Find Closest Person


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff_x = abs(x - z)
        diff_y = abs(y - z)
        if diff_x < diff_y:
            return 1
        elif diff_x > diff_y:
            return 2
        else:
            return 0


ans = Solution().findClosest(2, 7, 4)
print(ans)
