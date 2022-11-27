# 46. Permutations

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        temp = []
        for num in nums:
            for sub in result:
                for i in range(len(sub) + 1):
                    temp.append(sub[:i] + [num] + sub[i:])
            result = temp
            temp = []
        # # List comperhension:
        # for num in nums:
        #     result = [sub[:i] + [num] + sub[i:] for sub in result for i in range(len(sub) + 1)]
        return result


# class Solution:
#     def permutation(self, nums, li):
#         for i in nums:
#             li.append(i)
#             subset = nums.copy()
#             subset.remove(i)
#             if len(subset) == 0:
#                 self.ans.append(li.copy())
#             else:
#                 self.permutation(subset, li)
#             li.pop()

#     def permute(self, nums):
#         self.ans = []
#         li = []
#         self.permutation(nums, li)
#         return self.ans


# ans = Solution().permute([1, 2, 3])
ans = Solution().permute([1, 2, 3, 2])
print(ans)
