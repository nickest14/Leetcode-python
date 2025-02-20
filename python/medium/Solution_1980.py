# 1980. Find Unique Binary String

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result: list[str] = []
        for i in range(len(nums)):
            if nums[i][i] == "0":
                result.append("1")
            else:
                result.append("0")

        return "".join(result)


ans = Solution().findDifferentBinaryString(["111", "011", "001"])
print(ans)
