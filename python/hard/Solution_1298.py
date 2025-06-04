# 1298. Maximum Candies You Can Get from Boxes
from typing import List
from collections import deque


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        q: deque[int] = deque()
        for box_id in initialBoxes:
            for key in keys[box_id]:
                status[key] = 1

            if status[box_id] == 0:
                q.append(box_id)
            else:
                q.appendleft(box_id)

        ans: int = 0
        while q:
            ind = q.popleft()
            if status[ind] == 0:
                break
            elif status[ind] == 1:
                ans += candies[ind]
                for key in keys[ind]:
                    status[key] = 1

            for new_box_ind in containedBoxes[ind]:
                if status[new_box_ind] == 0:
                    q.append(new_box_ind)
                else:
                    q.appendleft(new_box_ind)

        return ans


status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
ans = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)

print(ans)
