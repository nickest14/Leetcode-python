# 2981. Find Longest Special Substring That Occurs Thrice I

from collections import defaultdict
from itertools import groupby


class Solution:
    def maximumLength(self, s: str) -> int:
        dic = defaultdict(int)
        subs = [''.join(sub) for _, sub in groupby(s)]
        for sub in subs:
            dic[sub] += 1
            if len(sub) > 1:
                dic[sub[1:]] += 2
            if len(sub) > 2:
                dic[sub[2:]] += 3

        return max(map(len, filter(lambda x: dic[x] > 2, dic)), default=-1)


ans = Solution().maximumLength('abcaba')
# ans = Solution().maximumLength('aaaabbbbbb')
print(ans)
