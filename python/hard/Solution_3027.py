# 3027. Find the Number of Ways to Place People II


from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        ans: int = 0
        n: int = len(points)

        for i in range(n):
            upper_y = points[i][1]
            lower_y_limit = float("-inf")
            for j in range(i + 1, n):
                current_y = points[j][1]
                if current_y <= upper_y and current_y > lower_y_limit:
                    ans += 1
                    lower_y_limit = current_y
                    if current_y == upper_y:
                        break
        return ans


ans = Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]])
print(ans)
