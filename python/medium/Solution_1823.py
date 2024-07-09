# 1823. Find the Winner of the Circular Game

from typing import List


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle: List[int] = [i for i in range(1, n + 1)]
        cur_ind: int = 0

        while len(circle) > 1:
            remove_ind: int = (cur_ind + k - 1) % len(circle)
            circle.pop(remove_ind)
            cur_ind = remove_ind

        return circle[0]


ans = Solution().findTheWinner(5, 2)
print(ans)
