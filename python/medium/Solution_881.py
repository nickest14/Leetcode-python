# 881. Boats to Save People

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1
        return ans


ans = Solution().numRescueBoats([1, 5, 3, 4], 6)
print(ans)
