# 1701. Average Waiting Time

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = curr = 0
        for arrival, time in customers:
            curr = max(curr, arrival) + time
            wait += curr - arrival

        return wait / len(customers)


ans = Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]])
print(ans)
