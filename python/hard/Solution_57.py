# 45. Jump Game II


class Solution:
    def insert(self, intervals, newInterval):
        len_intervals = len(intervals)
        if len_intervals == 0:
            return [newInterval]
        left_index, right_index = -1, -1
        find_left = False
        for m in range(0, len_intervals):
            if not find_left and newInterval[0] <= intervals[m][1]:
                find_left = True
                left_index = m
            if find_left:
                if newInterval[1] >= intervals[m][0]:
                    right_index = m
        if -1 == left_index:
            intervals.append(newInterval)
            return intervals
        new_intervals = []
        for m in range(0, left_index):
            new_intervals.append(intervals[m])
        add_interval = None
        start_index = -1
        if -1 != right_index:
            add_interval = [min(newInterval[0], intervals[left_index][0]), max(
                newInterval[1], intervals[right_index][1])]
            start_index = right_index + 1
        else:
            add_interval = newInterval
            start_index = left_index
        new_intervals.append(add_interval)
        for m in range(start_index, len_intervals):
            new_intervals.append(intervals[m])

        return new_intervals


intervals = [[1, 2], [8, 12], [15, 20], [21, 24], [27, 30]]
newInterval = [13, 25]
ans = Solution().insert(intervals, newInterval)
print(ans)
