# 1310. XOR Queries of a Subarray

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        length: int = len(arr)
        prefixs: list[int] = [0] * length
        ans: list[int] = []

        prefixs[0] = arr[0]
        for i in range(1, length):
            prefixs[i] = prefixs[i - 1] ^ arr[i]

        for left, right in queries:
            if left == 0:
                ans.append(prefixs[right])
            else:
                ans.append(prefixs[right] ^ prefixs[left - 1])
        return ans


ans = Solution().xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]])
print(ans)
