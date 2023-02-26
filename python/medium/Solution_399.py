# 399. Evaluate Division

from typing import List


import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        quot = collections.defaultdict(dict)
        for (s, d), v in zip(equations, values):
            quot[s][s] = 1.0
            quot[s][d] = v
            quot[d][s] = 1 / v
        for m in quot:
            for s in quot[m]:
                for d in quot[m]:
                    print(f'{m=} {s=} {d=}')
                    quot[s][d] = quot[s][m] * quot[m][d]
        return [quot[s].get(d, -1.0) for s, d in queries]


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Solution().calcEquation(equations, values, queries)
