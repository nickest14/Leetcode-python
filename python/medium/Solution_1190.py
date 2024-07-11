# 1190. Reverse Substrings Between Each Pair of Parentheses

from typing import List


class Solution:
    def reverseParentheses(self, s: str) -> str:
        n: int = len(s)
        stack: List[str] = []
        pair: dict = {}
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        result: List[str] = []
        i: int = 0
        direction: int = 1
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                direction *= -1
            else:
                result.append(s[i])
            i += direction

        return "".join(result)


ans = Solution().reverseParentheses("(ed(et(oc))el)")
print(ans)
