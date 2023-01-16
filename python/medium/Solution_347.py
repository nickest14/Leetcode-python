# 347. Top K Frequent Elements

from typing import List
import heapq
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)

        res = []
        for val, count in dic.items():
            if len(res) < k:
                heapq.heappush(res, (count, val))
            else:
                heapq.heappush(res, (count, val))
                heapq.heappop(res)
        return [val for count, val in res]


ans = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(ans)