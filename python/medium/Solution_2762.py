# 2762. Continuous Subarrays

from collections import defaultdict
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans: int = 0
        left: int = 0
        dic = defaultdict(int)

        for right in range(len(nums)):
            dic[nums[right]] += 1
            while max(dic.keys()) - min(dic.keys()) > 2:
                dic[nums[left]] -= 1

                if dic[nums[left]] == 0:
                    del dic[nums[left]]
                left += 1

            ans += right - left + 1

        return ans


ans = Solution().continuousSubarrays([5, 4, 2, 4])
# ans = Solution().continuousSubarrays([65,66,67,66,66,65,64,65,65,64])
print(ans)
