# 826. Most Profit Assigning Work

from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        ans = 0
        job = 0
        p = 0
        for w in worker:
            while job < len(jobs) and jobs[job][0] <= w:
                p = max(p, jobs[job][1])
                job += 1
            ans += p

        return ans


difficulty = [2, 4, 6, 8, 10]
profit = [10, 100, 30, 40, 50]
worker = [4, 5, 6, 7]
ans = Solution().maxProfitAssignment(difficulty, profit, worker)
print(ans)
