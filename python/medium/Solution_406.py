# 406. Queue Reconstruction by Height

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda p: (p[0], -p[1]), reverse=True)
        for _, p in enumerate(people):
            ans.insert(p[1], p)
        return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
ans = Solution().reconstructQueue(people)
print(ans)
