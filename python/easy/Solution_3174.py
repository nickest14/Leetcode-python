# 3174. Clear Digits

class Solution:
    def clearDigits(self, s: str) -> str:
        stack: list[str] = []
        for c in s:
            if c.isdigit():
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


ans = Solution().clearDigits('cb34')
print(ans)
