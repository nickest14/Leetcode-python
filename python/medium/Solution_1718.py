# 1718. Construct the Lexicographically Largest Valid Sequence

from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans: list[int] = [0] * (2 * n - 1)
        used: list[bool] = [False] * (n + 1)

        def dfs(i: int):
            if i >= (2 * n - 1):
                return True
            for x in range(n, 0, -1):
                # x > 1, we check two places. Mind index out of bound here.
                # x = 1, we only check one place
                # ans[i] == 0 means index i is not occupied
                if (
                    x > 1
                    and (
                        (not (ans[i] == 0 and (i + x < 2 * n - 1) and ans[i + x] == 0))
                        or used[x]
                    )
                ) or (x == 1 and (ans[i] != 0 or used[x])):
                    continue

                if x > 1:
                    ans[i] = x
                    ans[i + x] = x
                else:
                    ans[i] = x
                used[x] = True

                # find the next available place
                next_i = i + 1
                while next_i < 2 * n - 1 and ans[next_i]:
                    next_i += 1

                if dfs(next_i):
                    return True  # if it success, it is already the lexicographically largest one

                # backtracking, restore the state
                if x > 1:
                    ans[i] = 0
                    ans[i + x] = 0
                else:
                    ans[i] = 0
                used[x] = False

            return False

        dfs(0)

        return ans


for i in range(20):
    ans = Solution().constructDistancedSequence(i)
    print(ans)
