# 56. Merge Intervals


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals:
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output


ans = Solution().merge([[15, 18], [1, 3], [2, 6], [8, 10]])
print(ans)
