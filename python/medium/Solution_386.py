# 386. Lexicographical Numbers

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans: list[int] = []
        cur: int = 1
        for _ in range(n):
            ans.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10
        return ans


ans = Solution().lexicalOrder(10)
print(ans)
