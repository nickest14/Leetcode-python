# 1942. The Number of the Smallest Unoccupied Chair

from typing import List
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n: int = len(times)
        arrivals: list[tuple[int, int]] = [(times[i][0], i) for i in range(n)]
        arrivals.sort()

        available_chairs = list(range(n))
        leaving_queue: list[tuple[int, int]] = []

        for arrival_time, friend in arrivals:
            while leaving_queue and leaving_queue[0][0] <= arrival_time:
                released_chair: int = heapq.heappop(leaving_queue)[1]
                heapq.heappush(available_chairs, released_chair)

            chair = heapq.heappop(available_chairs)
            if friend == targetFriend:
                return chair

            heapq.heappush(leaving_queue, (times[friend][1], chair))

        return -1


# ans = Solution().smallestChair([[1,4],[2,3],[4,6]], 1)
ans = Solution().smallestChair([[3,10],[1,5],[2,6]], 0)
print(ans)
