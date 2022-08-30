# 228. Summary Ranges

from typing import List
import itertools
import operator


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        groups = itertools.groupby(enumerate(nums),
                                   key=lambda enum: enum[1] - enum[0])
        ans = []
        for _, values in groups:
            values = list(map(operator.itemgetter(1), values))
            if values[0] == values[-1]:
                ans.append(str(values[0]))
            else:
                ans.append(f'{values[0]}->{values[-1]}')
        return ans


ans = Solution().summaryRanges([-20, -18, -16, 5, 6, 7, 10])
print(ans)
