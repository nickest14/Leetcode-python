# 921. Minimum Add to Make Parentheses Valid


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack: list[str] = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)

        return len(stack)


ans = Solution().minAddToMakeValid('()))')
print(ans)
