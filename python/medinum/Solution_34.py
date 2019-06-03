# 34. Find First and Last Position of Element in Sorted Array


class Solution:
    def searchRange(self, nums, target):
        try:
            begin_index = nums.index(target)
            end_index = begin_index
            length = len(nums)
            while True and end_index+1 < length:
                if nums[end_index+1] == target:
                    end_index += 1
                else:
                    break
            return [begin_index, end_index]
        except:
            return [-1, -1]


# ans = Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
ans = Solution().searchRange(
    [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, ], 1)
print(ans)
