# 1233. Remove Sub-Folders from the Filesystem

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans: list[str] = [folder[0]]
        for i in range(1, len(folder)):
            last: str = ans[-1] + '/'
            if not folder[i].startswith(last):
                ans.append(folder[i])

        return ans


ans = Solution().removeSubfolders(['/a', '/a/b', '/c/d', '/c/d/e', '/c/f'])
print(ans)
