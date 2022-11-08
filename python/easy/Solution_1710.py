# 1710. Maximum Units on a Truck

from typing import List
import operator


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key=operator.itemgetter(1), reverse=True)
        for boxes, units in boxTypes:
            if truckSize < boxes:
                ans += truckSize * units
                break
            ans += boxes * units
            truckSize -= boxes
        return ans


ans = Solution().maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10)
print(ans)
