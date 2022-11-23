# 18. 4Sum

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def NSum(N: int, start: int, target: int, prefix: List[int]) -> List[List[int]]:
            if len(nums) - start < N:
                return None
            result = []
            if N == 2:
                end = len(nums) - 1
                while start < end:
                    if nums[start] + nums[end] < target:
                        start += 1
                    elif nums[start] + nums[end] > target:
                        end -= 1
                    else:
                        result.append(prefix + [nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end - 1] == nums[end]:
                            end -= 1
                        start += 1
                        end -= 1
            else:
                for i in range(start, len(nums) - N + 1):
                    if i > start and nums[i - 1] == nums[i]:
                        continue
                    result += NSum(N - 1, i + 1, target - nums[i], prefix + [nums[i]])
            return result

        nums.sort()
        return NSum(4, 0, target, [])


ans = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
print(ans)
