# 57. Insert Interval

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        ans.append(newInterval)

        return ans


# ans = Solution().insert([[7, 10]], [1, 5])
# ans = Solution().insert([[1, 3], [5, 8]], [4, 9])
ans = Solution().insert([[1, 3], [6, 9]], [2, 5])
print(ans)
