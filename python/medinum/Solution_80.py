class Solution:
    def removeDuplicates(self, nums) -> int:
        if nums:
            index = 0
            value = nums[0]
            temp_count = 1
            for i in range(1, len(nums)):
                if nums[i] == value:
                    temp_count += 1
                    if temp_count > 2:
                        continue
                    index += 1
                    nums[index] = value
                else:
                    value = nums[i]
                    index += 1
                    nums[index] = value
                    temp_count = 1
            return index + 1
        else:
            return 0


ans = Solution().removeDuplicates([2, 7, 7, 7, 7, 11, 15])
print(ans)
