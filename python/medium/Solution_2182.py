# 2182. Construct String With Repeat Limit

from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq: list[tuple[int]] = [(-ord(k), v) for k, v in Counter(s).items()]
        heapify(pq)

        ans: list[str] = []
        while pq:
            ch_ord, count = heappop(pq)
            ch = chr(-ch_ord)
            used = min(repeatLimit, count)
            ans.append(ch * used)
            count -= used

            if count > 0:
                if not pq:
                    break
                next_ch_ord, next_count = heappop(pq)
                ans.append(chr(-next_ch_ord))
                next_count -= 1

                if next_count > 0:
                    heappush(pq, (next_ch_ord, next_count))
                heappush(pq, (ch_ord, count))

        return ''.join(ans)


ans = Solution().repeatLimitedString('cczazcc', 3)
print(ans)
