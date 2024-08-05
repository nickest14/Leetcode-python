# 3016. Minimum Number of Pushes to Type Word II

from typing import List
from collections import Counter
import heapq


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq: dict[str, int] = Counter(word)
        heap: list[(int, int)] = []
        for char, freq in freq.items():
            heapq.heappush(heap, (-freq, char))

        ans: int = 0
        count: int = 1

        while heap:
            freq, _ = heapq.heappop(heap)
            freq = -freq

            if count <= 8:
                ans += freq
            elif count <= 16:
                ans += freq * 2
            elif count <= 24:
                ans += freq * 3
            else:
                ans += freq * 4

            count += 1

        return ans


# ans = Solution().minimumPushes('xyzxyzx')
ans = Solution().minimumPushes('xyzxyzxyzxyz')
# ans = Solution().minimumPushes('aabbccddeeffgghhiiiiii')
print(ans)
