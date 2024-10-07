# 2696. Minimum String Length After Removing Substrings


class Solution:
    def minLength(self, s: str) -> int:
        stack: list[str] = []
        for c in s:
            if stack and stack[-1] + c in ('AB', 'CD'):
                stack.pop()
            else:
                stack.append(c)

        return len(stack)


ans = Solution().minLength('ABFCACDB')
print(ans)
