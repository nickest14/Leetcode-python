# 1792. Maximum Average Pass Ratio

from heapq import heappop, heappush
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n: int = len(classes)
        impacts: list[tuple] = []

        for i in range(n):
            pass_count, total_count = classes[i][0], classes[i][1]
            cur_ratio: float = pass_count / total_count
            expected_ratio: float = (pass_count + 1) / (total_count + 1)
            impact = expected_ratio - cur_ratio
            heappush(impacts, (-impact, pass_count, total_count))

        while extraStudents > 0:
            _, pass_count, total_count = heappop(impacts)
            pass_count += 1
            total_count += 1
            cur_ratio: float = pass_count / total_count
            expected_ratio: float = (pass_count + 1) / (total_count + 1)
            impact = expected_ratio - cur_ratio

            heappush(impacts, (-impact, pass_count, total_count))
            extraStudents -= 1

        ans: float = 0
        for _, pass_count, total_count in impacts:
            ans += pass_count / total_count

        return ans / n


ans = Solution().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2)
print(ans)
