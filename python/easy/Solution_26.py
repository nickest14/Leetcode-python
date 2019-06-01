# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            index = 0
            value = nums[0]
            for i in range(1, len(nums)):
                if nums[i] == value:
                    continue
                else:
                    value = nums[i]
                    index += 1
                    nums[index] = value
            return index + 1
        else:
            return 0


ans = Solution().removeDuplicates([2, 7, 7, 7, 7, 11, 15])
print(ans)
