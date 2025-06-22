# 2138. Divide a String Into Groups of Size k

from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans: List[str] = []
        cur: int = 0
        n: int = len(s)
        while cur < n:
            ans.append(s[cur : cur + k])
            cur += k
        if len(ans[-1]) < k:
            ans[-1] += fill * (k - len(ans[-1]))

        return ans


ans = Solution().divideString("abcdefghi", 3, "x")
print(ans)
