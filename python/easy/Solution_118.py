# 118. Pascal's Triangle

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]  # layer 1
        for layer in range(2, numRows + 1):  # layer 2 to n
            tmp = [1]
            for i in range(1, layer - 1):
                tmp.append(ans[-1][i] + ans[-1][i - 1])
            tmp.append(1)
            ans.append(tmp)

        return ans


# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
ans = Solution().generate(5)
print(ans)

