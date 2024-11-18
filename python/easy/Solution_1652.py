# 1652. Defuse the Bomb

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for _ in code]
        ans: list[int] = code
        code = code * 2
        length: int = len(ans)
        for i in range(len(ans)):
            if k > 0:
                ans[i] = sum(code[i + 1: i + k + 1])
            else:
                ans[i] = sum(code[length + i + k:length + i])
        return ans


ans = Solution().decrypt([5, 7, 1, 4], 3)
# ans = Solution().decrypt([2, 4, 9, 3], -2)
print(ans)
