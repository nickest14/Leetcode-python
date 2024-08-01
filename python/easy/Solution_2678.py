# 2678. Number of Senior Citizens

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([int(detail[11:13]) > 60 for detail in details])


ans = Solution().countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"])
print(ans)
