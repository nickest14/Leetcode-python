# 1717. Maximum Score From Removing Substrings

from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            point = x
            lower_point = y
            pattern = 'ab'
            lower_pattern = 'ba'

        else:
            point = y
            lower_point = x
            pattern = 'ba'
            lower_pattern = 'ab'

        ans = 0
        stack: List[str] = []
        for c in s:
            if c == pattern[1] and stack and stack[-1] == pattern[0]:
                stack.pop()
                ans += point
            else:
                stack.append(c)

        lower_stack: List[str] = []
        for c in stack:
            if c == lower_pattern[1] and lower_stack and lower_stack[-1] == lower_pattern[0]:
                lower_stack.pop()
                ans += lower_point
            else:
                lower_stack.append(c)

        return ans


ans = Solution().maximumGain('cdbcbbaaabab', 4, 5)
print(ans)
