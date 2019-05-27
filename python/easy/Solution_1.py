class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in data.keys():
                return [data[ans], i]
            data[nums[i]] = i
        return []


ans = Solution().twoSum([2, 7, 11, 15], 9)
print(ans)
