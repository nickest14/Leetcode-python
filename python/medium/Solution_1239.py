# 1239. Maximum Length of a Concatenated String with Unique Characters

from typing import List
from collections import Counter


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char_set = set()

        def overlap(char_set, s):
            c = Counter(char_set) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):
            if i == len(arr):
                return len(char_set)
            ans = 0
            if not overlap(char_set, arr[i]):
                for c in arr[i]:
                    char_set.add(c)
                ans = backtrack(i + 1)
                for c in arr[i]:
                    char_set.remove(c)
            return max(ans, backtrack(i + 1))  # do not concatenate arr[i]

        return backtrack(0)


ans = Solution().maxLength(["un", "iq", "ue"])
print(ans)
