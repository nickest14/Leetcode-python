# 787. Cheapest Flights Within K Stops


from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = {src: 0}
        for _ in range(k + 1):
            update_dist, is_done = dict(dist.items()), True
            for u, v, w in flights:
                if dist.get(u, float('inf')) + w < update_dist.get(v, float('inf')):
                    update_dist[v] = dist[u] + w
                    is_done = False
            dist = update_dist
            if is_done:
                break
        return dist[dst] if dst in dist else -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
ans = Solution().findCheapestPrice(n, flights, src, dst, k)
print(ans)
