# 739. Daily Temperatures

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for ind, val in enumerate(temperatures):
            if stack and stack[-1][0] < val:
                while stack and stack[-1][0] < val:
                    data = stack.pop()
                    previous_index = data[1]
                    ans[previous_index] = ind - previous_index
                stack.append((val, ind))
            else:
                stack.append((val, ind))

        return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
ans = Solution().dailyTemperatures(temperatures)

print(ans)
