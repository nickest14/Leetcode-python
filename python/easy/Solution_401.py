# 401. Binary Watch

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for hh in range(12):
            for mm in range(60):
                if f'{hh:b}{mm:b}'.count('1') == turnedOn:
                    ans.append(f'{hh}:{mm:02d}')
        return ans


ans = Solution().readBinaryWatch(5)
print(ans)
