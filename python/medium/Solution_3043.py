# 3043. Find the Length of the Longest Common Prefix

from collections import defaultdict
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        dict_1: dict[str, int] = defaultdict(int)
        max_len: int = 0
        for i in range(len(arr1)):
            str1: str = ''
            for j in str(arr1[i]):
                str1 += j
                dict_1[str1] += 1
        for i in range(len(arr2)):
            str2: str = ''
            for j in str(arr2[i]):
                str2 += j
                if str2 in dict_1:
                    max_len = max(max_len, len(str2))

        return max_len


ans = Solution().longestCommonPrefix([1, 10, 100], [1000])
print(ans)
