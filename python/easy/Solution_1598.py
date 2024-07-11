# 1598. Crawler Log Folder

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        paths: List[str] = []
        for log in logs:
            if log == '../':
                if paths:
                    paths.pop()
            elif log != './':
                paths.append(log)

        return len(paths)


ans = Solution().minOperations(["d1/", "d2/", "../", "d21/", "./"])
print(ans)
