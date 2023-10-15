# 22. Generate Parentheses

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(open_n, close_n):
            if open_n == close_n == n:
                ans.append("".join(stack))
                return
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, close_n)
                stack.pop()
            if close_n < open_n:
                stack.append(")")
                backtrack(open_n, close_n + 1)
                stack.pop()

        backtrack(0, 0)
        return ans


ans = Solution().generateParenthesis(3)
print(ans)
