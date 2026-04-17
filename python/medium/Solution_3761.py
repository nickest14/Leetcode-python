# 3761. Minimum Absolute Distance Between Mirror Pairs

from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans: int = 10**5
        seen: dict[str, int] = {}

        for i, num in enumerate(nums):
            if num in seen:
                ans = min(ans, i - seen[num])
            seen[int(str(num)[::-1])] = i

        return ans if ans != 10**5 else -1


ans = Solution().minMirrorPairDistance( [12,21,45,33,54])
print(ans)
