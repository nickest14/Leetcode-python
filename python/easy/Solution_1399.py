# 1399. Count Largest Group

from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups: dict[int, int] = defaultdict(int)
        prev_sum: int = 0
        for i in range(1, n + 1):
            if i % 10 == 0:
                prev_sum = sum(int(c) for c in str(i))
            else:
                prev_sum += 1
            groups[prev_sum] += 1
        max_group: int = max(groups.values())

        return sum(1 for v in groups.values() if v == max_group)


ans = Solution().countLargestGroup(13)
print(ans)
