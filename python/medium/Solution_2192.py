# 2192. All Ancestors of a Node in a Directed Acyclic Graph

from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def dfs(i: int, cur: int):
            for c in child[cur]:
                if not ans[c] or ans[c][-1] != i:
                    ans[c].append(i)
                    dfs(i, c)

        ans = [[] for _ in range(n)]
        child = [[] for _ in range(n)]

        for e in edges:
            child[e[0]].append(e[1])
        for i in range(n):
            dfs(i, i)

        return ans


n = 8
edgeList = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
ans = Solution().getAncestors(n, edgeList)
print(ans)
