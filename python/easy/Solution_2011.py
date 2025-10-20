# 2011. Final Value of Variable After Performing Operations

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans: int = 0
        for op in operations:
            if op[0] == "+" or op[2] == "+":
                ans += 1
            else:
                ans -= 1
        return ans


ans = Solution().finalValueAfterOperations(["--X", "X++", "X++"])
print(ans)
