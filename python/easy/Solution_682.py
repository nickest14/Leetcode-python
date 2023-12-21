# 682. Baseball Game

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        for o in operations:
            if o == "+" and len(score_stack) >= 2:
                score_stack.append(score_stack[-1] + score_stack[-2])
            elif o == "D" and len(score_stack) >= 1:
                score_stack.append(score_stack[-1] * 2)
            elif o == "C" and len(score_stack) >= 1:
                score_stack.pop()
            else:
                score_stack.append(int(o))
        return sum(score_stack)


ans = Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
print(ans)
