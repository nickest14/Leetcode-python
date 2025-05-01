# 2071. Maximum Number of Tasks You Can Assign

from typing import List


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        def check_assign(mid: int, pills: int) -> bool:
            nonlocal n, tasks, workers
            i = 0
            j = n - mid
            queue: int = []
            
            while j < n:
                w = workers[j]
                while i < mid and tasks[i] <= w + strength:
                    queue += [tasks[i]]
                    i += 1

                if not queue:
                    return False
                
                if queue[0] <= w:
                    queue.pop(0)
                elif queue[0] > w and pills == 0:
                    return False
                else:
                    pills -= 1
                    queue.pop()
                j += 1
            return True

        tasks.sort()
        workers.sort()
        m, n = len(tasks), len(workers)
        ans: int = 0
        low: int = 0
        high: int = min(m, n)
        while low <= high:
            mid = (low + high) // 2
            if check_assign(mid, pills):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


ans = Solution().maxTaskAssign([3, 2, 1], [0, 3, 3], 1, 1)
print(ans)
