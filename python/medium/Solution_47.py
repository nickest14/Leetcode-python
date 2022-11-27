# 47. Permutations II

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        temp = []
        for num in nums:
            for sub in result:
                for i in range((sub + [num]).index(num) + 1):
                    temp.append(sub[:i] + [num] + sub[i:])
            result = temp
            temp = []
        # # List comperhension:
        # for num in nums:
        #     result = [sub[:i] + [num] + sub[i:] for sub in result for i in range((sub + [num]).index(num) + 1)]
        return result


ans = Solution().permuteUnique([1, 1, 2])
print(ans)
