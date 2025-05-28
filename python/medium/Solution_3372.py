# 3372. Maximize the Number of Target Nodes After Connecting Trees I

from typing import List


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        def dfs(node: int, k: int, adj: List[List[int]], par: int) -> int:
            cnt: int = 1
            if k > 0:
                for neighbor in adj[node]:
                    if neighbor != par:
                        cnt += dfs(neighbor, k - 1, adj, node)
            return cnt

        n1: int = len(edges1) + 1
        n2: int = len(edges2) + 1
        adj1: List[List[int]] = [[] for _ in range(n1)]
        adj2: List[List[int]] = [[] for _ in range(n2)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        if k == 0:
            return [1] * n1

        maxi: int = 0
        for i in range(n2):
            cnt: int = dfs(i, k - 1, adj2, -1)
            maxi = max(maxi, cnt)

        ans: List[int] = []
        for i in range(n1):
            cnt: int = dfs(i, k, adj1, -1)
            ans.append(cnt + maxi)

        return ans


ans = Solution().maxTargetNodes(
    [[0, 1], [0, 2], [2, 3], [2, 4]],
    [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
    2,
)
print(ans)
