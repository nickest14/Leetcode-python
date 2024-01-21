# 560. Subarray Sum Equals K

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum = 0, 0
        dic = {0: 1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in dic:
                count += dic[sum - k]
            dic[sum] = dic.get(sum, 0) + 1
        return count


ans = Solution().subarraySum([1, 2, 3, 4, 3, -2], 5)
print(ans)
