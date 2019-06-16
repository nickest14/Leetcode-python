# 32. Longest Valid Parentheses


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maxLen = 0
        last = -1
        for i in range(len(s)):
            print(stack)
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    last = i
                else:
                    stack.pop()
                    if not stack:
                        maxLen = max(maxLen, i - last)
                    else:
                        maxLen = max(maxLen, i - stack[-1])
                        print(f'maxlen = {maxLen}')

        return maxLen


ans = Solution().longestValidParentheses('(()))()')
print(ans)
