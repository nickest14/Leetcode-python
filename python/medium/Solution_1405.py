# 1405. Longest Happy String

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq: list[tuple[int, str]] = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        ans: str = ''
        while len(pq) > 1:
            freq1, c1 = heapq.heappop(pq)
            freq1 = -freq1
            if len(ans) <= 1 or (ans[-1] != c1 or ans[-2] != c1):
                ans += c1
                freq1 -= 1
                if freq1 > 0:
                    heapq.heappush(pq, (-freq1, c1))
            else:
                freq2, c2 = heapq.heappop(pq)
                freq2 = -freq2
                ans += c2
                freq2 -= 1
                if freq2 > 0:
                    heapq.heappush(pq, (-freq2, c2))
                if freq1 > 0:
                    heapq.heappush(pq, (-freq1, c1))
        if len(pq) == 1:
            freq1, c1 = heapq.heappop(pq)
            freq1 = -freq1
            if freq1 <= 1:
                ans += c1
            else:
                ans += c1 * 2

        return ans


ans = Solution().longestDiverseString(1, 1, 7)
print(ans)
